import string
with open("words.txt") as fin:
    s = fin.readline().split(",")
    letter_to_value = {letter: value+1 for (value, letter) in enumerate(string.ascii_uppercase)}
    triangle_numbers = set(int(0.5*n*(n+1)) for n in range(1000))
    print(sum(1 for word in s if sum(letter_to_value[i] for i in word.strip('"')) in triangle_numbers))
