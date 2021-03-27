
TELEPHONE_FIELD = {
    "1": [" "],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "0": ["-"]
}

def translateString(command):
    number = ""
    for char in command:
        for num in TELEPHONE_FIELD.keys():
            if char in TELEPHONE_FIELD[num]:
                number += num
    print(number)

def translateNumeric(command):
    possible_chars = []
    for num in command:
        possible_chars.append(TELEPHONE_FIELD[num])
    print(possible_chars)
    possible_words = calc_combinations(possible_chars, [[]], 1)
    print(possible_words)

def calc_combinations(charset, words, length):
    if charset == []:
        return words
    else:
        charset_length = len(charset[0])
        words_length = len(words)
        for i in range(length - 1):
            for word in range(words_length):
                words.append(words[word])
        if words_length < charset_length:
            for y in range(charset_length - words_length):
                words.append([])
        for char in range(charset_length):
            for pos in range(length):
                print(get_array_position(pos, char, length), words[get_array_position(pos, char, length)])
                words[get_array_position(pos, char, length)].append(charset[0][char])
        charset.pop(0)
        return calc_combinations(charset, words, charset_length)
            
def get_array_position(pos1, pos2, length):
    return ((pos1 * pos2) * length) + pos1


if __name__ == '__main__':
    print("What should be \"translated\"?")
    command = input()
    if command.isnumeric():
        translateNumeric(command)
    else:
        translateString(command)