class Rectangle():
    def __init__(self, rect, index=None):
        self.x, self.y, self.w, self.h = rect
        self.index = index
    def __repr__(self):
        return "(x = {}, y = {}, w = {}, h = {})".format(self.x, self.y, self.w, self.h)
    def intersect(self, rect):
        return (self.x < rect.x < self.x+self.w and self.y < rect.y < self.y+self.h) or (self.x < rect.x+rect.w < self.x+self.w and self.y < rect.y+rect.h < self.y+self.h) or (
                    rect.x < self.x < rect.x+rect.w and rect.y < self.y < rect.y+rect.h) or (rect.x < self.x+self.w < rect.x+rect.w and rect.y < self.y+self.h < rect.y+rect.h)


def read(text):
    with open(text) as fin:
        N = int(fin.readline())
        X, Y = [int(i) for i in fin.readline().split()]
        return [Rectangle((int(x), int(y), int(w), int(h)), i) for i, (x, y, w, h) in enumerate([i.split() for i in fin.readlines()])], (X, Y)



