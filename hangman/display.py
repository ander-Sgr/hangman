class HangmanDisplay:
    def __init__(self, hangman_states: list[str]) -> None:
        self.hangman_states = hangman_states

    def get_total_attempts(self) -> int:
        return len(self.hangman_states)

    def display_hangman(self, attempts_left: int) -> None:
        if attempts_left >= 0 and attempts_left < len(self.hangman_states):
            print(self.hangman_states[attempts_left])

    def display_presentation(self, word: str) -> None:
        total_letters = len(word)
        total_attempts = self.get_total_attempts()
        print("Welcome to the Hangman game!")
        print(f"The word has {total_letters} letters in total: {'_ ' * total_letters}")
        print(f"You have {total_attempts} attempts. ¡Good Luck!")
        print("==============================================")
