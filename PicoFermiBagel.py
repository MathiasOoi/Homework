import random
import unittest

class Test(unittest.TestCase):
    def test_valid_guess(self):
        self.assertFalse(validGuess("123", "1233"))
        self.assertTrue(validGuess("123", "789"))
        self.assertTrue(validGuess("16", "84"))
        self.assertFalse(validGuess("54", "ab"))
        self.assertFalse(validGuess("123", "113"))
        self.assertFalse(validGuess("78", "345"))

def validGuess(num, guess):
    # Checks for 3 things
    # 1. If the length of guess is equal to the length of the secret number
    # 2. If all characters in guess are unique
    # 3. If all characters in guess are integers
    return len(num) == len(guess) and len(set(guess)) == len(guess) and all(i in [str(n) for n in range(10)] for i in guess)

def GetSecretNumber(n):
    usedNumbers, num = set(), ""
    while len(num) != n:
        x = random.randint(0, 10)
        if x not in usedNumbers:
            num += str(x)
            usedNumbers.add(x)
    return num

def PicoFermiBagel(num, guess):
    output = []
    for i in range(len(guess)):
        if guess[i] == num[i]:
            output.append("Fermi")
        elif guess[i] in num:
            output.append("Pico")
    return " ".join(sorted(output)) if output else "Bagel"

def PlayGame():
    num = GetSecretNumber(int(input("How many digits do you want?")))
    print(num)
    while True:
        guess = input("Guess a number")
        if guess == num:
            if input('You Win!\nDo you want to play again? (type "yes")').lower() == "yes":
                PlayGame()
                break
        elif validGuess(num, guess):
            print(PicoFermiBagel(num, guess))
        else:
            print("Please enter a valid guess")



if __name__ == "__main__":
    unittest.main(exit=False)
    PlayGame()


