from CollisionDetection import *
from collections import defaultdict

class SpatialHash():
    def __init__(self, rectangles, dimensions):
        self.rectangles = rectangles
        self.MAX_X = dimensions[0]
        self.MAX_Y = dimensions[1]
        self.bin_size = max(dimensions)//4
        self.bins = []
        self.d = defaultdict(list)

    def create_bins(self):
    # Create a list of bins of bin_size by bin_size
        x = 0
        while x < self.MAX_X:
            y = 0
            while y < self.MAX_Y:
                self.bins.append(getPoints([x, y, self.bin_size, self.bin_size]))
                y += self.bin_size
            x += self.bin_size

    def insert_rects(self):
        # Put a rect inside of a bin if it intersects with the bin
        for i, bin in enumerate(self.bins):
            for k, rect in enumerate(self.rectangles):
                if intersect(bin, getPoints(rect)):
                    self.d[i].append(k)

    def solve(self):
    # Do N^2 comparison for every bin
        self.create_bins()
        self.insert_rects()
        results = set()
        for rects_in_bin in self.d.values():
            for a in rects_in_bin:
                for b in rects_in_bin:
                    if intersect(getPoints(self.rectangles[a]), getPoints(self.rectangles[b])) and (b, a) not in results:
                        results.add((a, b))
        return results



