#ifndef CH_H
#define CH_H

#include <vector>

struct Point {
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
};

int orientation(const Point& p, const Point& q, const Point& r);
std::vector<Point> convexHull(std::vector<Point>& points);

#endif // CH_H
