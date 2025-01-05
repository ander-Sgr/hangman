from random import randrange
from typing import List


class WordManagerError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WordManager:
    def __init__(self, words_list: List[str]) -> None:
        if not self.is_string_list(words_list):
            raise WordManagerError("The list does not contain strings")
        self.words_list: List[str] = words_list

    def get_random_word(self) -> str:
        size: int = len(self.words_list)
        if size != 0:
            r: int = randrange(size)
            random_word: str = self.words_list[r]
            return random_word
        else:
            raise WordManagerError("Error no word found")

    @staticmethod
    def is_string_list(words: List[str]) -> bool:
        for elem in words:
            if not isinstance(elem, str):
                return False
        return True
