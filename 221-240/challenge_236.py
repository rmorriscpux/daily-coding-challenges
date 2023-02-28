'''
You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon.
You can assume these points are given in order; that is, you can construct the polygon by connecting point 1 to point 2,
point 2 to point 3, and so on, finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, you should return False).
'''

# Assumptions:
# - All points used to set up a polygon are unique.
# - No intersecting lines exist in the polygon. (e.g. an 'hourglass' shape with lines crossing in the middle)
# - All points' x coordinates are less than sys.maxsize. (Python integers are capable of exceeding sys.maxsize)

import sys

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point{str(self)}"

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Line[{str(self.p1)}-{str(self.p2)}]"

class Polygon:
    # By definition, a polygon has at minimum three vertices/sides.
    def __init__(self, point1: Point, point2: Point, point3: Point, *addl_points: Point):
        # Build lines that form the polygon from the points input.
        self.lines = [Line(point1, point2), Line(point2, point3)]
        cur_point = point3
        for next_point in addl_points:
            self.lines.append(Line(cur_point, next_point))
            cur_point = next_point
        self.lines.append(Line(cur_point, point1))

    def isOnLine(self, line: Line, p: Point) -> bool:
        return (
            p.x <= min(line.p1.x, line.p2.x) and
            p.y <= min(line.p1.y, line.p2.y) and
            p.x <= max(line.p1.x, line.p2.x) and
            p.y <= max(line.p1.y, line.p2.y)
            )

    def getDirection(self, p1: Point, p2: Point, p3: Point) -> int:
        dir_val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y)

        if dir_val == 0:
            return 0
        elif dir_val < 0:
            return -1
        # else dir_val > 0
        return 1

    def isIntersecting(self, l1: Line, l2: Line) -> bool:
        dir1 = self.getDirection(l1.p1, l1.p2, l2.p1)
        dir2 = self.getDirection(l1.p1, l1.p2, l2.p2)
        dir3 = self.getDirection(l2.p1, l2.p2, l1.p1)
        dir4 = self.getDirection(l2.p1, l2.p2, l1.p2)

        return (
            (dir1 != dir2 and dir3 != dir4) or
            (dir1 == 0 and self.isOnLine(l1, l2.p1)) or
            (dir2 == 0 and self.isOnLine(l1, l2.p2)) or
            (dir3 == 0 and self.isOnLine(l2, l1.p1)) or
            (dir4 == 0 and self.isOnLine(l2, l1.p2))
        )

    def pointIsInside(self, p: Point) -> bool:
        # Draw a horizontal line from p to an arbitrarily high x coordinate.
        check_line = Line(p, Point(sys.maxsize, p.y))
        # Count intersections between the check_line and all lines in the polygon.
        count = 0
        for line in self.lines:
            if self.isIntersecting(line, check_line):
                if not self.getDirection(line.p1, p, line.p2):
                    # Special case: Returns False when p lies exactly on the line.
                    return self.isOnLine(line, p)
                count += 1

        # p is within the polygon when the horizontal line formed from it intersects an odd number of the polygon's sides.
        return count % 2 == 1

if __name__ == "__main__":
    poly = Polygon(
        Point(-5, -5),
        Point(-5, 5),
        Point(5, 5),
        Point(5, -5)
    )

    print(poly.pointIsInside(Point(2, 3)))
    print(poly.pointIsInside(Point(-7, 3)))
    print(poly.pointIsInside(Point(5, 3)))
    print(poly.pointIsInside(Point(2, 5)))