import java.util.ArrayList;
import java.util.List;

class Point {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class ConvexHull {
    public static int orientation(Point p, Point q, Point r) {
        int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
        if (val == 0) return 0; // Collinear
        return (val > 0) ? 1 : 2; // Clockwise or Counterclockwise
    }

    public static List<Point> convexHull(Point[] points) {
        int n = points.length;
        if (n < 3) return new ArrayList<>();

        List<Point> hull = new ArrayList<>();
        int l = 0;
        for (int i = 1; i < n; i++)
            if (points[i].y < points[l].y || (points[i].y == points[l].y && points[i].x < points[l].x))
                l = i;

        int p = l, q;
        do {
            hull.add(points[p]);
            q = (p + 1) % n;
            for (int i = 0; i < n; i++)
                if (orientation(points[p], points[i], points[q]) == 2)
                    q = i;
            p = q;
        } while (p != l);

        return hull;
    }
}