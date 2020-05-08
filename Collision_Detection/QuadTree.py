from CollisionDetection import *

class QuadTree():
    def __init__(self, x, y, dimensions, rectangles):
        self.rectangles = rectangles
        self.x = x
        self.y = y
        self.max_obj = 10
        self.max_depth = 4
        self.half_x = dimensions[0]//2 + 1
        self.half_y = dimensions[1]//2 + 1
        self.leaves = set()
        # Initially create 4 leaves that will later on subdivide into other QuadTrees
        self.quad1 = Leaf(self.x, self.y+self.half_y, (self.half_x, self.half_y), self.rectangles)
        self.quad2 = Leaf(self.x+self.half_x, self.y+self.half_y, (self.half_x, self.half_y), self.rectangles)
        self.quad3 = Leaf(self.x, self.y, (self.half_x, self.half_y), self.rectangles)
        self.quad4 = Leaf(self.x+self.half_x, self.y, (self.half_x, self.half_y), self.rectangles)
    def insert(self, rect_index):
        # Insert a rectangle into a Quadtree
        # If after inserting the rectangle there are more than max_obj in the leaf
        # Then .subdivide() the leaf
        if intersect(self.quad1.getPoints(), getPoints(self.rectangles[rect_index])):
            self.quad1.insert(rect_index)
            if len(self.quad1) > self.max_obj:
                self.quad1.subdivide()
        if intersect(self.quad2.getPoints(), getPoints(self.rectangles[rect_index])):
            self.quad2.insert(rect_index)
            if len(self.quad2) > self.max_obj:
                self.quad2.subdivide()
        if intersect(self.quad3.getPoints(), getPoints(self.rectangles[rect_index])):
            self.quad3.insert(rect_index)
            if len(self.quad3) > self.max_obj:
                self.quad3.subdivide()
        if intersect(self.quad4.getPoints(), getPoints(self.rectangles[rect_index])):
            self.quad4.insert(rect_index)
            if len(self.quad4) > self.max_obj:
                self.quad4.subdivide()
    def get_leaves(self, node):
        # Returns a list of tuples of leaves
        if type(node) == QuadTree:
            for child in [node.quad1, node.quad2, node.quad3, node.quad4]:
                self.get_leaves(child)
        else:
            self.leaves.add(tuple(node.rects))
    def solve(self):
        # Do N^2 comparison for every leaf
        for i, rect in enumerate(self.rectangles):
            self.insert(i)
        self.get_leaves(self)
        results = set()
        for quad in self.leaves:
            for i, a in enumerate(quad):
                for k, b in enumerate(quad):
                    if intersect(getPoints(self.rectangles[a]), getPoints(self.rectangles[b])) and (b, a) not in results:
                        results.add((a, b))
        return results

class Leaf():
    def __init__(self, x, y, dimensions, rectangles):
        self.rectangles = rectangles
        self.x = x
        self.y = y
        self.dimensions = dimensions
        self.MAX_X = dimensions[0]
        self.MAX_Y = dimensions[1]
        self.rects = []
        self.max_obj = 10
        self.max_depth = 5
    def insert(self, obj_index):
        self.rects.append(obj_index)
    def __len__(self):
        return len(self.rects)
    def subdivide(self):
        # Turns Leaf into a QuadTree with 4 leaves
        # If you at max_depth then set max_obj to infinity
        temp_rect = self.rects[:]
        out = QuadTree(self.x, self.y, self.dimensions, self.rectangles)
        out.max_depth -= 1
        if out.max_depth == 0:
            out.max_obj = float("inf")
        for rect in temp_rect:
            out.insert(rect)
    def getPoints(self):
        # Returns the dimensions of the leaf (quadrant)
        return (self.x, self.y), (self.x+self.MAX_X, self.y+self.MAX_Y)



