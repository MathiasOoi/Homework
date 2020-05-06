with open("simple.txt") as fin:
    N = int(fin.readline())
    X, Y = [int(i) for i in fin.readline().split()]
    rectangles = [(int(x), int(y), int(w), int(h)) for (x, y, w, h) in [i.split() for i in fin.readlines()]]

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

def bruteForce():
    # Solves in O(N^2)
    result = set()
    for i, a in enumerate(rectangles):
        for k, b in enumerate(rectangles):
            if i != k and intersect(getPoints(a), getPoints(b)) and (k, i) not in result:
                result.add((i, k))
    return result

if __name__ == "__main__":
    print(bruteForce())