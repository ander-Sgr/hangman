class HangmanDisplay:
    def __init__(self, hangman_states: list[str]) -> None:
        self.hangman_states = hangman_states

    def get_total_attempts(self) -> int:
        return len(self.hangman_states)

    def display_hangman(self, attempts_left: int) -> None:
        print(self.hangman_states[attempts_left])

    def display_presentation(self, word: str, attempts: int) -> None:
        total_letters = len(word)
        print("Welcome to the Hangman game!")
        print("The word has", total_letters, "letters in total", "_ " * total_letters)
        print("You have", attempts, "attempts. ¡Good Luck!")
