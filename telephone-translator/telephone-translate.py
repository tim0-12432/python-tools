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

characters = {1: "", 2:"abc", 3:"def",4 :"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz", 0: "-"}

def translateString(command):
    number = ""
    for char in command:
        for num in TELEPHONE_FIELD.keys():
            if char in TELEPHONE_FIELD[num]:
                number += num
    return number


def translateNumeric(command):
    words = []
    if len(command) == 0:
        return "Type in a number!"
    possible_words = []
    permutations(command, characters, possible_words)
    for word in possible_words:
        if translateString(word) == command:
            print(f"Validating ... {possible_words.index(word) + 1} from {len(possible_words)} ...")
            if check_word(word):
                words.append(word)
    return words


def permutations(digits, chars, result, curr_string="", curr_level=0):
    if curr_level == len(digits):
        result.append(curr_string)
        return
    for i in chars[int(digits[curr_level])]:
        permutations(digits, chars, result, curr_string + i, curr_level + 1)


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