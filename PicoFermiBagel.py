# 1. Implement the following bots, ALL with the limited access to game (get digits, take guess only)
#  - Brute force
#  - Eliminite-then-iterate (your Bot)
#  - Hypothesis-elimination (Tim's bot v1)
#  - Optimized hypothesis elimination (Tim's bot v2)

import random
import unittest
import itertools
import time
from collections import defaultdict

class BruteForceBot:
    def __init__(self, game):
        self.game = game
        self.to_guess = list(itertools.permutations("0123456789", self.game.numDigits()))

    def get_guess(self):
        return "".join(self.to_guess.pop())

    def play(self):
        while True:
            guess = self.get_guess()
            p, f = self.game.takeGuess(guess)
            if f == self.game.numDigits():
                print("Bot guess is {}".format(guess))
                break

class EliminateThenIterateBot:
    def __init__(self, game):
        self.game = game

    def play(self):
        print("Secret num: {}".format(self.game.num))
        # Suggestion - add a function to Game that says "printDebug()"
        bagel = ""
        for i in itertools.combinations("012345789", self.game.numDigits()):
            if self.game.takeGuess(i) == (0, 0):
                bagel = i
                break
        print("Bagel {}".format(bagel))
        nums_in_secret = []
        for i in set("0123456789").difference(bagel):
            if max(self.game.takeGuess("".join(bagel[:self.game.numDigits() - 1]) + i)) == 1:
                nums_in_secret.append(i)
        print(nums_in_secret)
        for k in itertools.permutations(nums_in_secret, self.game.numDigits()):
            if self.game.takeGuess("".join(k))[1] == self.game.numDigits():
                print("Bot guess is {}".format("".join(k)))
                break


class Bot:
    def __init__(self, game):
        self.game = game
        self.possible = list(itertools.permutations("012345789", self.game.numDigits()))

    def play(self):
        p, f = 0, 0
        while f != self.game.numDigits():
            guess = random.choice(self.possible)
            p, f = self.game.takeGuess(guess)

            # Knowing that possible[i] results in (p,f) means we can limit ourselves
            # only to those possibilities that are still consistent
            self.possible = [hypo for hypo in self.possible if (p, f) == PicoFermiBagel(hypo, guess)]
        print("Bot guess is {}".format("".join(guess)))

class OptimizedBot:
    def __init__(self, game):
        self.game = game
        self.possible = list(itertools.permutations("012345789", self.game.numDigits()))
        self.outcomes = self.initializeOutcome(self.game.numDigits())
        self.k = 0


    def initializeOutcome(self, n):
        return [(p, f) for p in range(n + 1) for f in range(n + 1) if p + f <= n]

    def getPossibleOutcomes(self):
        return set(outcome for outcome in self.outcomes if sum(outcome) >= self.k)

    def getElims(self, guess):
        omap = defaultdict(int)
        for k in self.possible:
            omap[PicoFermiBagel(k, guess)] += 1
        return min(omap.values())
    def getNextGuess(self):
        bestGuess, mostElims = (), 0
        for guess in self.possible:
            x = self.getElims(guess)
            if x > mostElims:
                bestGuess, mostElims = guess, x
        return bestGuess

    def play(self):
        print(self.game.num)
        guess = random.choice(self.possible)
        p, f = self.game.takeGuess(guess)
        self.possible = [hypo for hypo in self.possible if (p, f) == PicoFermiBagel(hypo, guess)]
        while f != self.game.numDigits():
            print(self.possible)
            self.k = p + f
            guess = self.getNextGuess()
            p, f = self.game.takeGuess(guess)
            self.possible = [hypo for hypo in self.possible if (p, f) == PicoFermiBagel(hypo, guess)]
        print("Bot guess is {}".format("".join(guess)))


class Game:
    def __init__(self, n):
        self.n = n
        self.num = self.getSecretNumber()

    def numDigits(self):
        return self.n

    def getSecretNumber(self):
        num = random.randint(10 ** (self.n - 1), (10 ** self.n) - 1)
        return str(num) if self.validGuess(str(num)) else self.getSecretNumber()

    def validGuess(self, guess):
        # Checks for 3 things
        # 1. If the length of guess is equal to the length of the secret number
        # 2. If all characters in guess are unique
        # 3. If all characters in guess are integers
        return self.n == len(guess) and len(set(guess)) == len(guess) and all(i in "0123456789" for i in guess)

    def takeGuess(self, guess):
        return PicoFermiBagel(self.num, guess)


def PicoFermiBagel(num, guess):
    Fermi, Pico = 0, 0
    for i in range(len(guess)):
        if guess[i] == num[i]:
            Fermi += 1
        elif guess[i] in num:
            Pico += 1
    return Pico, Fermi



def test(n, bots):
    for bot in bots:
        print(bot)
        game = Game(n)
        print("Secret num is {}".format(game.num))
        start = time.time()
        bot(game).play()
        print("Time: {}".format(time.time()-start), end="\n\n")


if __name__ == "__main__":
    #test(3, [BruteForceBot, EliminateThenIterateBot, Bot])
    x = OptimizedBot(Game(3))
    print(x.outcomes)
    x.play()








