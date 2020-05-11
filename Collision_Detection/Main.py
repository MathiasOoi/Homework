import time
from BruteForce import BruteForce
from SpatialHash import SpatialHash
from QuadTree import QuadTree
from CollisionDetection import *



if __name__ == "__main__":
    docs = ["1.Simple.txt", "2.Medium.txt", "3.Mixed.txt"]
    for text in docs:
        print(text)
        rects, dimensions = read(text)
        start = time.time()
        x = BruteForce(rects)
        print("BruteForce:")
        print("Solution: " + str(x.solve()))
        print("Time: " + str(time.time() - start) + "\n")
        start = time.time()
        x = SpatialHash(rects, dimensions)
        print("SpatialHash:")
        print("Solution: " + str(x.solve()))
        print("Time: " + str(time.time() - start) + "\n")
        start = time.time()
        x = QuadTree(Rectangle((0, 0, dimensions[0], dimensions[1])), rects)
        print("QuadTree: ")
        print("Solution: " + str(x.solve()))
        print("Time: " + str(time.time() - start) + "\n")


