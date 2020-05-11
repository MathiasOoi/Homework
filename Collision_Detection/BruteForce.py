from CollisionDetection import *

class BruteForce():
    def __init__(self, rectangles):
        self.rectangles = rectangles
    def solve(self):
        result = set()
        for a in self.rectangles:
            for b in self.rectangles:
                if a.intersect(b) and (b.index, a.index) not in result:
                    result.add((a.index, b.index))
        return result

