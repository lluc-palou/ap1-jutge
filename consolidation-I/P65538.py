from yogi import read
from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class Word:
    word: str
    frequency: int

Words: TypeAlias = list[Word]

def most_frequent_word(L: list[str]) -> None:
    """Writes the most frequent word of the given sequence, whether if there is
    a tie, prints the larges word in alphabetical order. """

    List_Words: Words = []

    # Finds a list containing unique words in the sequence.
    U: list[str] = []

    for word in L:
        if word not in U:
            counter = 1
            U.append(word)
            One_Word = Word(word, counter)
            List_Words.append(One_Word)

        else:
            for A_Word in List_Words:
                if A_Word.word == word:
                    A_Word.frequency += 1
                    
    # Sorts the list of Words (unique words of the sequence with the corresponding frequencies),
    # in reversed alphabeticall order.
    List_Words.sort(key = lambda x: x.word, reverse = True)

    # Finds the most frequent word.
    max_frequency_1 = 0
    max_frequency_2 = 0
    index_1 = 0
    index_2 = 0

    for i in range(len(List_Words)):
        if List_Words[i].frequency > max_frequency_1:
            index_2 = index_1 
            max_frequency_2 = max_frequency_2
            index_1 = i
            max_frequency_1 = List_Words[i].frequency
    
    if max_frequency_1 == max_frequency_2:
        print(List_Words[index_2].word, end = '\n')
    
    else:
        print(List_Words[index_1].word, end = '\n')

def main() -> None:
    # Reads several cases, each beggin with (n) followed by (n) words,
    # the end of the input is denoted by using (n = 0).
    n = read(int)

    while n > 0:
        L: list[str] = []

        for _ in range(n):
            w = read(str)
            L.append(w)

        most_frequent_word(L)
        n = read(int)

if __name__ == '__main__':
    main()