s = 'abbaba'
def palindromes(s):
    numOfSubStr = 0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            # iterate over all possible substrings
            subStr = s[i:j]
            print(subStr)
            if len(subStr) < 2:
                pass
            elif subStr == subStr[::-1]:
                numOfSubStr += 1
    return numOfSubStr


print(palindromes(s))