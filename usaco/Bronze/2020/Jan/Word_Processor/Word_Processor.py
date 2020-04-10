with open("word.in") as fin:
    # Parse data
    n, k = [int(i) for i in fin.readline().split()]
    words = fin.readline().split()

with open("word.out", "w") as fout:
    l = len(words[0])
    # If the word can fir on the current line put it there
    # Otherwise write the word on a new line
    fout.write(words[0])
    for word in words[1:]:
        if l + len(word) > k:
            fout.write('\n' + word)
            l = len(word)
        else:
            fout.write(" ")
            fout.write(word)
            l += len(word)

