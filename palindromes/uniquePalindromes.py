s = 'bababa'
def uniquePalindromes(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            # iterate over all possible substrings
            subStr = s[i:j]
            if subStr == subStr[::-1]:
                if subStr not in palindromes:
                    palindromes.add(subStr)
    return len(palindromes)


print(uniquePalindromes(s))


