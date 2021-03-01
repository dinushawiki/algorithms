class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def is_ccw(point_a, point_b, point_c):
        area = ((point_b.x - point_a.x) * (point_c.y - point_a.y)) - ((point_b.y - point_a.y) * (point_c.x - point_a.x))
        if area < 0:
            return -1  # clockwise
        elif area > 0:
            return 1  # counter-clockwise
        else:
            return 0  # collinear


point_a = Point2D(0, 0)
point_b = Point2D(-2, 2)
point_c = Point2D(-1, 1)
print(Point2D.is_ccw(point_a, point_b, point_c))
