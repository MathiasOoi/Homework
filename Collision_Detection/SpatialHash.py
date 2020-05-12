from collections import defaultdict

class SpatialHash():
    def __init__(self, rectangles, dimensions):
        self.rectangles = rectangles
        self.MAX_X, self.MAX_Y = dimensions
        self.bin_size = 16
        self.bins = defaultdict(list)

    def get_bins(self, rect):
        min_x = rect.x // self.bin_size
        max_x = (rect.x + rect.w) // self.bin_size
        min_y = rect.y // self.bin_size
        max_y = (rect.y + rect.h) // self.bin_size
        return [(x, y) for x in range(min_x, max_x+1) for y in range(min_y, max_y+1)]

    def insert_rects(self):
        # Put a rect inside of a bin if it intersects with the bin
        for rect in self.rectangles:
            for key in self.get_bins(rect):
                self.bins[key].append(rect.index)

    def solve(self):
    # Do N^2 comparison for every bin
        self.insert_rects()
        results = set()
        for rects_in_bin in self.bins.values():
            for a in rects_in_bin:
                for b in rects_in_bin:
                    if self.rectangles[a].intersect(self.rectangles[b]) and (b, a) not in results:
                        results.add((a, b))
        return results



