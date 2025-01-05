from display import HangmanDisplay
from words import WordManager
from config import Config


class Game:
    def __init__(self, random_word: WordManager, display: HangmanDisplay):
        self.random_word = random_word.get_random_word()
        self.attempts_left = display.get_total_attempts()
        self.guessed_letters = set()
        self.display = display.display_presentation(
            self.random_word, self.attempts_left
        )
        self.lines = [self.random_word]

    def display_lines(self, lines):
        for char in lines[0]:
            if char in self.guessed_letters:
                print(char, end=' ')
            else:
                print("_", end=' ')

    def valid_input(self, letter):
        is_valid = True
        if len(letter) > 1 or len(letter) == 0:
            is_valid = False
        return is_valid

    def enter_letter(self, lines):
        letter = input("Enter a letter: ")
        if not self.valid_input(letter):
            print("The input should be a one letter")
            return
        for char in lines[0]:
            if letter == char:
                print(letter, end=' ')
        
        
    def start(self):
        self.enter_letter(self.lines)
        self.display_lines(self.lines)


# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
words = ["bananas"]
random_word = WordManager(words)
display = HangmanDisplay(Config.HANGMAN_STATES)
init_game = Game(random_word, display)


init_game.start()
