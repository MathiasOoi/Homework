import random
import math
import time

class Rectangle:
    def __init__(self, dimensions):
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
def writeInput(n):
    # Input format
    # The first line contains N, the next N lines contains two integers w, l
    # Were w is the width and l in the length
    with open("rect.in", "w") as fout:
        fout.write(str(n) + "\n")
        for _ in range(n):
            fout.write("%s %s\n"%(random.randint(1, 9), random.randint(1, 9)))

def parseInput():
    with open("rect.in") as fin:
        n = int(fin.readline())
        rects = [Rectangle(tuple(int(k) for k in i.split())) for i in fin]
        #print(rects)
        return rects, n


def oneLayer(rects):
    # Puts all rectangles in one row
    rectCopy = rects.copy()
    currx = 0
    for i in range(len(rectCopy)):
        rectCopy[i].updateCords(currx, 0)
        currx += rectCopy[i].w
    return rectCopy[-1].x


def greedy(rects, n):
    # Place sqrt of amount of rectangles in one row
    # Keep on repeating that until there are no more rectangles
    sortedRects = sorted(rects, key=lambda x: -x.h) # Sorts rects by height
    rectsPerLayer = math.ceil(math.sqrt(n))
    maxy, maxX = 0, 0
    for i in range(0, n, rectsPerLayer):
        currx, y = 0, 0
        for k in range(i, i+rectsPerLayer):
            if k + 1 > n:
                break
            sortedRects[k].updateCords(currx, maxy)
            currx += sortedRects[k].w
            if sortedRects[k].h > y:
                y = sortedRects[k].h
        maxy += y
        if currx > maxX:
            maxX = currx
    return max(maxX, maxy)

def test(cases):
    for i, k in enumerate(cases):
        writeInput(k)
        rects, n = parseInput()
        print("n = %s"%(k))
        start = time.time()
        print("oneLayer: %s"%(oneLayer(rects)))
        print("time: %s"%(time.time()-start))
        start = time.time()
        print("greedy: %s"%(greedy(rects, n)))
        print("time: %s\n"%(time.time()-start))

test([10, 50, 100, 500, 1000])

