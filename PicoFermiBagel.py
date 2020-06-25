import random
import unittest
import itertools
import time

class Test(unittest.TestCase):
    pass
#    def test_valid_guess(self):
#        self.assertFalse(validGuess("123", "1233"))
#        self.assertTrue(validGuess("123", "789"))
#        self.assertTrue(validGuess("16", "84"))
#        self.assertFalse(validGuess("54", "ab"))
#        self.assertFalse(validGuess("123", "113"))
#        self.assertFalse(validGuess("78", "345"))

class BruteForceBot:
    def __init__(self, n=2):
        self.game = Game(n)
        self.to_guess = list(itertools.permutations("0123456789", n))
    def get_guess(self):
        return "".join(self.to_guess.pop())
    def play(self):
        print("Secret num: {}".format(self.game.num))
        while True:
            n = self.get_guess()
            if n == self.game.num:
                print("Success secret num was {}".format(n))
                break

class Bot:
    def __init__(self, n=2):
        self.n = n
        self.game = Game(n)
    def get_bagel_guess(self):
        return "".join(self.check_for_bagel.pop())
    def play(self):
        print("Secret num: {}".format(self.game.num))
        bagel = ""
        for i in itertools.combinations("012345789", self.n):
            if self.game.PicoFermiBagel(i) == "Bagel":
                bagel = i
                break
        print("Bagel {}".format(bagel))
        nums_in_secret = [i for i in set("0123456789").difference(bagel) if self.game.PicoFermiBagel("".join(bagel[:self.n-1]) + i) == "Pico" or self.game.PicoFermiBagel("".join(bagel[:self.n-1]) + i) == "Fermi"]
        print(nums_in_secret)
        for k in itertools.permutations(nums_in_secret, self.n):
            if "".join(k) == self.game.num:
                print("Success secret num was {}".format("".join(k)))
                break





class Game:
    def __init__(self, n):
        self.n = n
        self.num = self.getSecretNumber()

    def getSecretNumber(self):
        num = random.randint(10**(self.n-1), (10**self.n)-1)
        return str(num) if self.validGuess(str(num)) else self.getSecretNumber()

    def validGuess(self, guess):
        # Checks for 3 things
        # 1. If the length of guess is equal to the length of the secret number
        # 2. If all characters in guess are unique
        # 3. If all characters in guess are integers
        return self.n == len(guess) and len(set(guess)) == len(guess) and all(i in "0123456789" for i in guess)

    def PicoFermiBagel(self, guess):
        output = []
        for i in range(len(guess)):
            if guess[i] == self.num[i]:
                output.append("Fermi")
            elif guess[i] in self.num:
                output.append("Pico")
        return " ".join(sorted(output)) if output else "Bagel"



def PlayGame():
    pass
#    num = GetSecretNumber(int(input("How many digits do you want?")))
#    print(num)
#    while True:
#        guess = input("Guess a number")
#        if guess == num:
#            if input('You Win!\nDo you want to play again? (type "yes")').lower() == "yes":
#                PlayGame()
#                break
#        elif validGuess(num, guess):
#            print(PicoFermiBagel(num, guess))
#        else:
#            print("Please enter a valid guess")


def test(n, bots):
    for bot in bots:
        print(str(bot)[17:-2])
        start = time.time()
        bot(n).play()
        print(time.time() - start, end="\n\n")

if __name__ == "__main__":
#    unittest.main(exit=False)
    test(8, [BruteForceBot, Bot])



