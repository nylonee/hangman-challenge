import random
from functools import reduce

content = ['mary', 'had', 'a', 'little', 'lamb']

class HangmanGenerator:
    def __init__(self, death_in=15):
        self._word = None
        self.death_in = death_in
        self.letters_tried = []

    def start(self):
        line = content[0]
        for num, aline in enumerate(content):
            if random.randrange(num + 2): continue
            line = aline

        self._word = line
        print("The game of Hangman has started!")
        print("")
        print("The word is {} letters long".format(len(self._word)))

    def word(self):
        curr_word = reduce((lambda x, y: x + y), [self._word[num] if l in self.letters_tried else "_" for num, l in enumerate(self._word)])

        print("The current word is {}".format(curr_word))
        return curr_word

    def guess(self, letter):
        print("You have guessed '{}'".format(letter))

        if self.death(): return False

        if letter in self._word and letter not in self.letters_tried:
            print("Yay! You found a letter in the word!")
            self.letters_tried.append(letter)
            return True

        print("Sorry! The letter is not in the word =(")
        self.death_in -= 1
        return False

    def won(self):
        curr_word = reduce((lambda x, y: x + y), [self._word[num] if l in self.letters_tried else "_" for num, l in enumerate(self._word)])

        try:
            curr_word.index("_")
            return False
        except ValueError:
            print("You have won the game!")
            return True

    def death(self):
        if self.death_in <=0:
            print("You are dead!")
            return True
        return False
