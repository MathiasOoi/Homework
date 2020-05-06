import time
from collections import defaultdict
def read(text):
    with open(text) as fin:
        N = int(fin.readline())
        X, Y = [int(i) for i in fin.readline().split()]
        return [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in [i.split() for i in fin.readlines()]], (X, Y)

def getPoints(rectangle):
    # Takes in a tuple of (x, y, w, h)
    # Returns the 2 corners of a rectangle
    x, y, w, h = rectangle
    return [(x, y), (x+w, y+h)]

def intersect(rect1, rect2):
    # Check if a point is in the other rectangle
    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2
    return (x1 < x3 < x2 and y1 < y3 < y2) or (x1 < x4 < x2 and y1 < y4 < y2) or (x3 < x1 < x4 and y3 < y1 < y4) or (x3 < x2 < x4 and y3 < y2 < y4)

def bruteForce(rectangles, dimensions = None):
    # Solves in O(N^2)
    result = set()
    for i, a in enumerate(rectangles):
        for k, b in enumerate(rectangles):
            if i != k and intersect(getPoints(a), getPoints(b)) and (k, i) not in result:
                result.add((i, k))
    return result

def spatialHash(rectangles, dimensions):
    """
    :param rectangles: List of 2 corner points of a rectangle
    :param dimensions: Tuple of max x and max y
    :return:
    """
    bin_size = max(dimensions)//4
    # Create bins of bin_size by bin_size
    def create_bins():
        x, y, bins = 0, 0, []
        while x < dimensions[0]:
            while y < dimensions[1]:
                bins.append(getPoints([x, y, bin_size, bin_size]))
                y += bin_size
            x += bin_size
            y = 0
        return bins
    results, d, bins = set(), defaultdict(list), create_bins()
    bins = create_bins()
    # Maps bin to a list of rectangles that intersect with bin
    for i, bin in enumerate(bins):
        for k, rect in enumerate(rectangles):
            if intersect(bin, getPoints(rect)):
                d[i].append(k)
    # Do brute force on bin instead of doing brute force globally
    for in_bin in d.values():
        for a in in_bin:
            for b in in_bin:
                if intersect(getPoints(rectangles[a]), getPoints(rectangles[b])) and (b, a) not in results:
                    results.add((a, b))
    return results

def display(function, time_list, text):
    print(str(function).split()[1].title() + ":")
    for i, text in enumerate(text):
        start = time.time()
        rectangles, dimensions = read(text)
        solution = function(rectangles, dimensions)
        print(str(i + 1) + " " + text)
        time_list.append(time.time() - start)
        print("Time: " + str(time.time() - start))
        print("Solution: " + str(solution))
    print("\n")


if __name__ == "__main__":
    bf, sh, text = [], [], ["simple.txt", "medium.txt", "mixed.txt"]
    display(bruteForce, bf, text)
    display(spatialHash, sh, text)
    print("Comparisons")
    for i in range(3):
        print(text[i])
        print(bf[i] / sh[i])