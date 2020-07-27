import random
import os
random.seed(0) # Set seed for debugging

class Rectangle:
    def __init__(self, dimensions):
        # initialize dimensions and (x, y) position fo the rectangle
        self.w, self.h = dimensions
        self.x = None
        self.y = None
    def __repr__(self):
        return "(x = {}, y = {}, w = {}, h = {})".format(self.x, self.y, self.w, self.h)
    def updateCords(self, x, y):
        self.x, self.y = x, y
    def intersect(self, rect):
        return (self.x < rect.x < self.x+self.w and self.y < rect.y < self.y+self.h) or (self.x < rect.x+rect.w < self.x+self.w and self.y < rect.y+rect.h < self.y+self.h) or (
                    rect.x < self.x < rect.x+rect.w and rect.y < self.y < rect.y+rect.h) or (rect.x < self.x+self.w < rect.x+rect.w and rect.y < self.y+self.h < rect.y+rect.h)
    def corners(self):
        # Returns tuple of  corners of the rectangle (top left, top right, bottom left)
        return ((self.x + self.w, self.y), (self.x, self.y + self.h), (self.x + self.w, self.y + self.h))


def writeInput(n):
    # Input format
    # The first line contains N, the next N lines contains two integers w, l
    # Were w is the width and l in the length
    with open("rect.in", "w") as fout:
        fout.write(str(n) + "\n")
        for _ in range(n):
            fout.write("%s %s\n"%(random.randint(1, 9), random.randint(1, 9)))

def parseInput(file):
    # Returns a tuple of (rect and n)
    # rect: list of Rectangles
    # n: int
    with open(os.getcwd()+"\\cases\\{}".format(file)) as fin:
        n = int(fin.readline())
        rects = [Rectangle(tuple(int(k) for k in i.split())) for i in fin]
        return rects, n


with open(os.getcwd()+"\\cases\\index.txt") as fin:
    FILENAMES = [line.strip() for line in fin]
