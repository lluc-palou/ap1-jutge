from yogi import read, scan

def read_words() -> list[str]:
    """Reads the words from the dictionary and returns it as a list."""

    List = []
    word = scan(str)
    while word is not None:
        List.append(word)
        word = scan(str)
    return List

def apply_rules(hexagon: str, List: list[str]) -> list[str]:
    """Returns a list of words that fulfill the rules of the game, for every word:
        - Has a minimum of 3 letters.
        - Its letters are the letters in the hexagon word.
        - Contains the middle letter of the hexagon word."""
    
    # In case whether the word has an smaller lenght than 3 is deleted from the list.
    i = 0
    while i < len(List):
        if len(List[i]) < 3:
            List.pop(i)
            i -= 1
        i += 1
    
    # Checking whether its letters are in the hexagon word.
    letters_in_hexagon = list(hexagon)
    i = 0
    while i < len(List):
        j = 0
        middle_letter_found = False
        same_word = False
        while j < len(List[i]) and not same_word:
            k = 0
            some_letter_found = False
            while k < len(letters_in_hexagon) and not some_letter_found:
                if letters_in_hexagon[k] == List[i][j]:
                    some_letter_found = True
                k += 1
            if hexagon[0] == List[i][j]:
                middle_letter_found = True
            # In case that some letter does not appear in hexagon, the word is removed 
            # from the list.
            if not some_letter_found:
                List.pop(i)
                same_word = True
                i -= 1
            j += 1
        # In case that the word does not contain the middle letter of the hexagon word, 
        # the word is removed from the list.
        if not middle_letter_found:
            List.pop(i)
            i -= 1
        i += 1
    return List

def is_tuti(hexagon: str, word: str) -> bool:
    """Tells if the given word is a "tuti" following the term definition of the game."""

    # Converts the word to a list of unique letters.
    letters_of_word = list(word)
    i = 0
    while i < len(letters_of_word):
        j = i + 1
        while j > i and j < len(letters_of_word):
            if letters_of_word[i] == letters_of_word[j]:
                letters_of_word.pop(i)
                i -= 1
            j += 1
        i += 1

    # Checks whether is a "tuti".
    if sorted(letters_of_word) == sorted(list(hexagon)):
        return True
    else:
        return False

def compute_score(hexagon: str, List: list[str]) -> int:
    """Returns the score get by the words in the given list."""

    score = 0
    list_lenght = len(List)
    for i in range(list_lenght):
        word_lenght = len(List[i])
        if word_lenght== 3:
            score += 1
        elif word_lenght == 4:
            score += 2
        elif word_lenght >= 5:
            score += word_lenght
        if is_tuti(hexagon, List[i]):
            score += 10
    return score
    
def main() -> None:
    # Reads the first word that contais the letters of the hexagon and 
    # the remaining words from the dictionary.
    hexagon = read(str)
    Dictionary_words = read_words()

    # Apply the rules of the game and computes scores.
    List_of_words = apply_rules(hexagon, Dictionary_words)
    score = compute_score(hexagon, List_of_words)

    # Output, includes the list of words ordered alphabetically and the total score of the game.
    List_of_words = sorted(List_of_words)
    for i in range(len(List_of_words)):
        print(List_of_words[i], end = '\n')
    print('-----', end = '\n')
    print(score, end = '\n')

if __name__ == '__main__':
    main()