from random import randrange


class WordManagerError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class WordManager:
    def __init__(self, words_list: list[str]):
        if not self.is_string_list(words_list):
            raise WordManagerError("The list not contains strings")
        self.words_list = words_list

    def get_random_word(self):
        size = len(self.words_list)
        if size != 0:
            r = randrange(size)
            random_word = self.words_list[r]
            return random_word
        else:
            raise WordManagerError("Error no word found")

    @staticmethod
    def is_string_list(words: list[str]) -> bool:
        is_valid = True
        for elem in words:
            if not isinstance(elem, str):
                is_valid = False
        return is_valid
