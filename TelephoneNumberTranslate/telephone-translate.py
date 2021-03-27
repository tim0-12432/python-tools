
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
    return number


def translateNumeric(command):
    possible_chars = []
    for num in command:
        for char in TELEPHONE_FIELD[num]:
            possible_chars.append(char)
    charsAsString = ""
    for char in possible_chars:
        charsAsString += char
    possible_words = permutations(charsAsString)
    print(possible_words)


def permutations(remaining, candidate="", arr=[]):
    if len(arr) == 10:
        return arr

    if len(remaining) == 0:
        arr.append(candidate)

    for i in range(len(remaining)):
        newCandidate = candidate + remaining[i]
        newRemaining = remaining[0:i] + remaining[i+1:]
        permutations(newRemaining, newCandidate, arr)


if __name__ == '__main__':
    print("What should be \"translated\"?")
    command = input()
    if command.isnumeric():
        res = translateNumeric(command)
    else:
        res = translateString(command)
    print(res)