import time
from BruteForce import BruteForce
from SpatialHash import SpatialHash
from QuadTree import QuadTree
from CollisionDetection import read



if __name__ == "__main__":
    bf, sh, qt, docs = [], [], [], ["1.Simple.txt", "2.Medium.txt", "3.Mixed.txt"]
    for text in docs:
        print(text)
        rects, dimensions = read(text)
        # Brute Force
        start = time.time()
        x = BruteForce(rects)
        print("BruteForce:")
        print(str(x.solve()))
        print(time.time() - start)
        bf.append(time.time() - start)
        print()
        # Spatial Hash
        start = time.time()
        x = SpatialHash(rects, dimensions)
        print("SpatialHash:")
        print(str(x.solve()))
        print(time.time() - start)
        sh.append(time.time() - start)
        print()
        # Quad Tree
        start = time.time()
        x = QuadTree(0, 0, dimensions, rects)
        print("QuadTree:")
        print(x.solve())
        print(time.time() - start)
        qt.append(time.time()-start)
        print()
    for i, doc in enumerate(docs):
        print(doc)
        print("BruteForce: " + str(bf[i]))
        print("SpatialHash: " + str(sh[i]))
        print("QuadTree: " + str(qt[i]))
        print()
