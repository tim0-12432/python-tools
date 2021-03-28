import enchant

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

LANGUAGE = "en_GB"


def translateString(command):
    number = ""
    for char in command:
        for num in TELEPHONE_FIELD.keys():
            if char in TELEPHONE_FIELD[num]:
                number += num
    return number


def translateNumeric(command):
    words = []
    possible_chars = []
    for num in command:
        possible_chars.append(TELEPHONE_FIELD[num])
    possible_words = permutations(possible_chars)
    for word in possible_words:
        if translateString(word) == command:
            if check_word(word):
                words.append(word)
    return words


def permutations(text):
    partial = []
    partial.append(text[0][0])

    for i in range(1, len(text)):
        for j in reversed(range(len(partial))):
            curr = partial.pop(j)

            for k in range(len(curr) + 1):
                partial.append(curr[:k] + text[i][0] + curr[k:])

    partial1 = []
    partial1.append(text[0][1])

    for i in range(1, len(text)):
        for j in reversed(range(len(partial1))):
            curr = partial1.pop(j)

            for k in range(len(curr) + 1):
                partial1.append(curr[:k] + text[i][0] + curr[k:])

    partial2 = []
    partial2.append(text[0][2])

    for i in range(1, len(text)):
        for j in reversed(range(len(partial2))):
            curr = partial2.pop(j)

            for k in range(len(curr) + 1):
                partial2.append(curr[:k] + text[i][0] + curr[k:])

    for p in partial1:
        partial.append(p)
    for p in partial2:
        partial.append(p)
    return partial


def check_word(word):
    dictionary = enchant.Dict(LANGUAGE)
    return dictionary.check(word)


if __name__ == '__main__':
    print("What should be \"translated\"?")
    command = input()
    if command.isnumeric():
        res = translateNumeric(command)
    else:
        res = translateString(command)
    print(res)