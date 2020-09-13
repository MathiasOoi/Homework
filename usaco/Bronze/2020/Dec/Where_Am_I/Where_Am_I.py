with open("whereami.in") as fin:
    n = int(fin.readline())
    mailboxes = fin.readline()
    print(n, mailboxes)

with open("whereami.out", "w") as fout:
    for k in range(3, n):
        lst = []
        for i in range(n-k+1):
            lst.append(mailboxes[i:i+k])
        print(lst)
        for _ in range(len(lst)):
            if lst.pop() in lst:
                break
        if not lst:
            fout.write(str(k))
            break
