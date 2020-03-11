def countMostCommonWords(textfile, limit=10):
    file = open(textfile, "r")
    words = file.readline()
    file.close()
    words = words.split()
    total = len(words)
    dictWords = {}
    for splits in words:
        if splits not in dictWords:
            dictWords[splits] = 1
        else:
            dictWords[splits] += 1
    for i in range(1, limit + 1):
        mostFreq = ''
        maxCount = 0
        for key in dictWords:
            if dictWords[key] > maxCount:
                maxCount = dictWords[key]
                mostFreq = key
        print(str(i) + ". Most common word: " + str(mostFreq) + " Count: " + str(maxCount) + " Percentage: " + str(round(maxCount/total, 5)))
        dictWords.pop(mostFreq)
    return ""


print(countMostCommonWords("words.txt"))
