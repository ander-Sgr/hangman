from .display import HangmanDisplay
from .words import WordManager
from .config import Config

class Game:

    hangman_states = HangmanDisplay(Config.HANGMAN_STATES)

    def __init__(self, random_word: WordManager, display: HangmanDisplay):
        self.random_word = random_word.get_random_word()
        self.attempts_left = display.get_total_attempts()
        self.guessed_letters = set()
        self.display = display.display_presentation(self.random_word)
        self.fields = [self.random_word]

    def display_field(self, fields):
        for char in fields[0]:
            if char in self.guessed_letters:
                print(char, end=" ")
            else:
                print("_", end=" ")
        print()

    def valid_input(self, letter):
        is_valid = False
        if len(letter) == 1 and letter.isalpha():
            is_valid = True
        return is_valid

    def is_letter_in_word(self, letter):
        if letter in self.random_word:
            return True
        return False

    def process_letter_guessed(self, letter):
        for char in self.fields[0]:
            if letter == char:
                self.guessed_letters.add(letter)

    def enter_letter(self):
        letter = input("Enter a letter: ")
        if not self.valid_input(letter):
            print("The input should be a one letter")
        self.check_input(letter)

    def check_input(self, letter):
        if self.is_letter_in_word(letter):
            print("Correct, the letter", letter, "is in the word")
            print("Progress: ")
            self.process_letter_guessed(letter)
            self.display_field(self.fields)
        else:
            print("Sorry, the letter", letter, "is not in the word")
            self.attempts_left -= 1
            print("You have", self.attempts_left, "attempts left")
            self.display_field(self.fields)
            index = len(Config.HANGMAN_STATES) - self.attempts_left
            self.hangman_states.display_hangman(index)

    def is_game_over(self):
        if set(self.random_word) == self.guessed_letters:
            print("Congrats you guessed the word:", self.random_word)
            return True
        if self.attempts_left <= 0:
            print("Game over! The word was:", self.random_word)
            return True
        return False

    def start(self):
        while not self.is_game_over():
            self.enter_letter()
