#include "ConvexHull.h"
#include <algorithm>

int orientation(const Point& p, const Point& q, const Point& r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0; // Collinear
    return (val > 0) ? 1 : 2; // Clockwise or Counterclockwise
}

std::vector<Point> convexHull(std::vector<Point>& points) {
    int n = points.size();
    if (n < 3) return {};

    // Sort points based on x-coordinate
    std::sort(points.begin(), points.end(), [](const Point& a, const Point& b) {
        return (a.x < b.x) || (a.x == b.x && a.y < b.y);
        });

    // Function to find lower hull
    auto lowerHull = [&]() -> std::vector<Point> {
        std::vector<Point> hull;
        for (int i = 0; i < n; ++i) {
            while (hull.size() >= 2 && orientation(hull[hull.size() - 2], hull[hull.size() - 1], points[i]) != 2)
                hull.pop_back();
            hull.push_back(points[i]);
        }
        hull.pop_back(); // Last point is the same as first point
        return hull;
        };

    std::vector<Point> lower = lowerHull();
    std::reverse(points.begin(), points.end());
    std::vector<Point> upper = lowerHull();

    // Combine lower and upper hull
    lower.insert(lower.end(), upper.begin(), upper.end());
    return lower;
}
