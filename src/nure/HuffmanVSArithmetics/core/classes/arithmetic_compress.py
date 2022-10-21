from typing import Optional, List
import numpy as np
from collections import Counter
from decimal import *


def get_intervals(probabilities, low, high) -> np.ndarray:
    interval_range = high - low
    intervals = []
    for prob in probabilities:
        new_high = prob * interval_range + low
        intervals.append([low, new_high])
        low = new_high

    return intervals


def interval_matching(intervals, value):
    for i, interval in enumerate(intervals):
        if interval[0] <= value < interval[1]:
            return i, interval


class ArithmeticCompress:
    __slots__ = ["__message", "encoded_message", "characters", "probabilities"]

    __message: str
    encoded_message: Optional[float]
    characters: List[str]
    probabilities: Optional[np.ndarray]

    def __init__(self, message, precision=500):
        self.__message = message
        self.encoded_message = None
        self.characters = []
        self.probabilities = None
        getcontext( ).prec = precision

    def encode_message(self):
        message_length = len(self.__message)
        counter = Counter(self.__message)
        high = Decimal(1.0)
        low = Decimal(0.0)

        # Sort a list of pairs (char, frequency) in descending order
        unique_chars = list(counter.keys( ))
        frequencies = list(counter.values( ))
        # probabilities = np.divide(np.array(frequencies),
        #                           np.array(message_length), dtype=np.longdouble)
        total_frequency = Decimal(message_length)
        probabilities = [Decimal(frequency) / total_frequency for frequency in frequencies]

        # A dictionary that translates a character to an index of subinterval
        char_index_table = dict(zip(unique_chars, np.arange(len(probabilities))))

        for char in self.__message:
            intervals = get_intervals(probabilities, low, high)
            interval = intervals[char_index_table[char]]
            high = interval[1]
            low = interval[0]

        self.characters = unique_chars
        self.probabilities = probabilities
        return low

    def decode_message(self, encoded_message, length) -> str:
        high = Decimal(1.0)
        low = Decimal(0.0)

        decoded_message = ''
        for _ in np.arange(length):
            intervals = get_intervals(self.probabilities, low, high)
            try:
                index, interval = interval_matching(intervals, encoded_message)
            except TypeError:
                print("Not enough precision! None interval is matched! ")
                break

            high = interval[1]
            low = interval[0]
            decoded_message += self.characters[index]

        return decoded_message
