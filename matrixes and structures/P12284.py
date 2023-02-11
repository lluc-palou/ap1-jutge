from yogi import read
from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class Word:
    unique_word: str
    frequency: int

Unique_word_list: TypeAlias = list[Word]

def most_frequent_words(Word_list: list[str], k: int) -> None:
    """Writes the (k) most frequent words contained in the given sequence (Word_list),
    whether there is a tie, the smaller word in alphabetical order is printed."""

    Unique_words: Unique_word_list = []

    # Creates a list of unique words with its frequencies corresponding to appearences
    # in the given sequence.
    for word in Word_list:
        found = False

        for u_word in Unique_words:
            if word == u_word.unique_word:
                u_word.frequency += 1
                found = True
        
        if not found:
            Unique_words.append(Word(word, 1))
    
    # Sorts the unique list of words by ascending order of the frequency atribute.
    Unique_words.sort(key = lambda x: x.frequency, reverse = True)

    # Writes the (k) most frequent words.
    i = 0
    counter = 0

    while i + 1 < len(Unique_words) and counter < k:
        if Unique_words[i].frequency == Unique_words[i + 1].frequency:
            if Unique_words[i + 1].unique_word < Unique_words[i].unique_word:
                print(Unique_words[i + 1].unique_word, end = '\n')
                del Unique_words[i + 1]
                counter += 1

            else:
                print(Unique_words[i].unique_word, end = '\n')
                del Unique_words[i]
                counter += 1

        else:
            print(Unique_words[i].unique_word, end = '\n')
            del Unique_words[i]
            counter += 1
    
    if counter < k:
        print(Unique_words[0].unique_word, end = '\n')
        
def main() -> None:
    # Reads several cases, each starting with (n), followed by (n) words.
    n = read(int)

    while n is not None:
        k = read(int)
        Word_list: list[str] = []

        # Reads the sequence of (n) words.
        for _ in range(n):
            word = read(str)
            Word_list.append(word)
        
        # Prints the output.
        most_frequent_words(Word_list, k)
        print('----------', end = '\n')

        n = read(int)

if __name__ == '__main__':
    main()