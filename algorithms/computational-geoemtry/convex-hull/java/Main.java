import java.util.ArrayList;
import java.util.List;

class Main {
    public static void main(String[] args) {
        Point[] points = {new Point(0, 3), new Point(1, 1), new Point(2, 2), new Point(4, 4),
                new Point(0, 0), new Point(1, 2), new Point(3, 1), new Point(3, 3)};

        List<Point> convexHullPoints = ConvexHull.convexHull(points);
        System.out.println("Convex Hull Points:");
        for (Point p : convexHullPoints)
            System.out.println("(" + p.x + ", " + p.y + ")");
    }
}
