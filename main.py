from hangman import Config, HangmanDisplay, Game, WordManager


def main():
    # Define the list of words
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    # Initialize the WordManager with the list of words
    word_manager = WordManager(words)

    # Initialize the HangmanDisplay with the hangman states from the config
    display = HangmanDisplay(Config.HANGMAN_STATES)

    # Initialize the Game with the WordManager and HangmanDisplay
    game = Game(word_manager, display)

    # Start the game
    game.start()


if __name__ == "__main__":
    main()
