from CollisionDetection import Rectangle

class QuadTree:
    def __init__(self, dimensions, rectangles, depth=5):
        """
        :param dimensions: Dimensions of QuadTree (rectangle)
        :param rectangles: List of objects of Rectangle
        """
        self.dimensions = dimensions
        self.rectangles = rectangles
        self.depth = depth
        self.leaves = []
        self.children = [Leaf(Rectangle((self.dimensions.x+(i*self.dimensions.w//2+1), self.dimensions.y+(k*self.dimensions.h//2+1), self.dimensions.w//2, self.dimensions.h//2)), self.rectangles, self.depth-1) for i in range(2) for k in range(2)]

    def insert(self, node, rect):
        """
        Insert a rect into a QuadTree
        If this causes a leaf to go beyond max_obj, subdivide the leaf
        :param node: A QuadTree
        :param rect: object of Rectangle
        """
        for i, child in enumerate(node.children):
            if type(child) == Leaf:
                if rect.intersect(child.dimensions):
                    child.insert_to_leaf(rect.index)
                    if len(child) > child.max_obj and bool(child.depth):
                        node.children[i] = child.subdivide()
            else:
                child.insert(child, rect)

    def traverse(self, parent):
        for child in self.children:
            if type(child) == Leaf:
                parent.leaves.append(child.leaf_rects)
            else:
                child.traverse(parent)

    def solve(self):
        for rect in self.rectangles:
            self.insert(self, rect)
        result = set()
        self.traverse(self)
        for leaves in self.leaves:
            for a in leaves:
                for b in leaves:
                    if self.rectangles[a].intersect(self.rectangles[b]) and (b, a) not in result:
                        result.add((a,b))
        return result


class Leaf:
    def __init__(self, dimensions, rectangles, depth):
        """
        :param dimensions: Dimensions of Tree (rectangle class)
        """
        self.dimensions = dimensions
        self.rectangles = rectangles
        self.leaf_rects = []  # List indexes of rectangles in the leaf
        self.max_obj = 12
        self.depth = depth
    def __len__(self):
        return len(self.leaf_rects)
    def insert_to_leaf(self, rect):
        self.leaf_rects.append(rect)
    def subdivide(self):
        """
        Create a new QuadTree and insert all the rects in this leaf
        to the new QuadTree
        :return: New QuadTree
        """
        tree = QuadTree(self.dimensions, self.rectangles, self.depth)
        for rect in self.leaf_rects:
            tree.insert(tree, self.rectangles[rect])
        return tree



