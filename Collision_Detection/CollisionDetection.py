class CollisionDetection():
    def __init__(self, rectangles, dimensions):
        self.rectangles = rectangles
        self.MAX_X = dimensions[0]
        self.MAX_Y = dimensions[1]


def read(text):
    with open(text) as fin:
        N = int(fin.readline())
        X, Y = [int(i) for i in fin.readline().split()]
        return [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in [i.split() for i in fin.readlines()]], (X, Y)


def getPoints(rect):
    """
    :param rect: Tuple of (x, y, w, h)
    :return: Tuple of (Bottom left cord, Top right cord)
    """
    x, y, w, h = rect
    return (x, y), (x + w, y + h)


def intersect(rect1, rect2):
    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2
    return (x1 < x3 < x2 and y1 < y3 < y2) or (x1 < x4 < x2 and y1 < y4 < y2) or (x3 < x1 < x4 and y3 < y1 < y4) or (x3 < x2 < x4 and y3 < y2 < y4)
