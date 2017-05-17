from worder import HangmanGenerator

def main():
    hangman = HangmanGenerator()
    # generates a random word, and starts the game
    hangman.start()

    # prints the current progress of the word
    hangman.word()

    # guesses the letter 'a' for the word
    hangman.guess('a')

    # returns true if game over and you were hung
    hangman.death()

if __name__ == "__main__":
	main()
