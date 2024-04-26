#include <iostream>
#include "ConvexHull.h"

int main() {
    std::vector<Point> points = { {0, 3}, {1, 1}, {2, 2}, {4, 4}, {0, 0}, {1, 2}, {3, 1}, {3, 3} };

    std::vector<Point> convexHullPoints = convexHull(points);
    std::cout << "Convex Hull Points:\n";
    for (const auto& p : convexHullPoints)
        std::cout << "(" << p.x << ", " << p.y << ")\n";

    return 0;
}
