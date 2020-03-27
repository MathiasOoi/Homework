set1 = set([1,2,3])
set2 = set()
if (set1 - set1.intersection(set2)).intersection(set2 - set1.intersection(set2)) == set():
    print("a")