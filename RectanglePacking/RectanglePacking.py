import random
import math
import time
from GenTestCases import *
import os


def oneLayer(rects):
    # Puts all rectangles in one row
    # returns length of square rectangles fit in, packing density
    rectCopy = rects.copy()
    currx = 0
    for i in range(len(rectCopy)):
        rectCopy[i].updateCords(currx, 0)
        currx += rectCopy[i].w
    return rectCopy[-1].x + rectCopy[-1].w, sum(x.w*x.h for x in rectCopy)/(rectCopy[-1].x + rectCopy[-1].w)**2


def greedy(rects, n):
    # Place sqrt of amount of rectangles in one row
    # Keep on repeating that until there are no more rectangles
    # returns length of square rectangles fit in, packing density
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
    return max(maxX, maxy), sum(x.w*x.h for x in sortedRects)/max(maxX, maxy)**2

def cornerGreedy(rects, n):
    # try placing a rectangle on every corner
    # if the rectangle can fit without expanding the grid then place it there
    # otherwise find a corner that would minimize the expansion of the grid
    # returns length of square rectangles fit in, packing density
    corners = [(0,0)] # list of available corners (x, y)
    sortedRects = sorted(rects, key=lambda x: -x.h*x.w) # Sort rects by decreasing area
    placed = []  # list of placed rectangles
    maxX, maxY = 0, 0
    for rect in sortedRects:
        rectCopy = rect
        bestPoint = (0, 0)  # (x, y) value of corner in which placing the rectangle would minimize expansion
        k = (float("inf"), float("inf"))  # (amount x would be expanded, amount y would be expanded)
        placedRect = False
        for corner in corners:
            rectCopy.updateCords(corner[0], corner[1])
            if all(not rectCopy.intersect(rectOnGrid) for rectOnGrid in placed):
                # check if rect can be placed here
                # i.e. check if it intersects with any placed rectangles
                xExpansion = rectCopy.w + corner[0]
                yExpansion = rectCopy.h + corner[1]
                if xExpansion > maxX or yExpansion > maxY:  # check if placing rect would cause grid to expand
                    # if so check if
                    if max(xExpansion, yExpansion) < max(k):
                        k = (xExpansion, yExpansion)
                        #print("Debug1: {}".format(k))
                        bestPoint = corner
                else:
                    bestPoint = corner
                    k = (0, 0)
                    break
        rect.updateCords(bestPoint[0], bestPoint[1])
        placed.append(rect)
        maxX += k[0] - rect.w
        maxY += k[1] - rect.h
        corners.remove(bestPoint)  # remove the point where rectangle was placed
        corners.extend(rect.corners())
        #print(maxX, maxY)
        #print(corners)
    #print(placed)
    return max(maxX, maxY), sum(x.w*x.h for x in sortedRects)/max(maxX, maxY)**2








def test():
    for file in FILENAMES:
        rects, n = parseInput(file)
        print(file[:-4])
        start = time.time()
        print("oneLayer: %s"%(str(oneLayer(rects))))
        print("time: %s"%(time.time()-start))
        start = time.time()
        print("greedy: %s"%(str(greedy(rects, n))))
        print("time: %s"%(time.time()-start))
        start = time.time()
        print("cornerGreedy: %s" % (str(cornerGreedy(rects, n))))
        print("time: %s\n" % (time.time() - start))

if __name__ == "__main__":
    test()


