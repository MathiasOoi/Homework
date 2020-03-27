def wordProcessor():
    file = open('word.in', 'r')
    l = file.readlines()
    file.close()
    n, k = l[0].split()
    words = l[1].split()
    out = open('word.out', 'w')
    length = 0
    for word in words:
        if length + len(word) > int(k):
            out.write('\n' + word)
            length = len(word)
        else:
            if length > 0:
                out.write(' ')
            out.write(word)
            length += len(word)
    out.close()
wordProcessor()
