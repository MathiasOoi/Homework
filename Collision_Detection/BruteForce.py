from CollisionDetection import *

class BruteForce():
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def solve(self):
        result = set()
        for i, a in enumerate(self.rectangles):
            for k, b in enumerate(self.rectangles):
                if i != k and intersect(getPoints(a), getPoints(b)) and (k, i) not in result:
                    result.add((i, k))
        return result


