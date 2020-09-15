def scoreWord(word):
    sum = 0
    for c in word:
        if (31 < ord(c) < 65) | (90 < ord(c) < 97) | (ord(c) > 122):
            sum += 0
        else:
            c_lower = ord(c.lower()) - 97
            sum += c_lower
    return sum

if __name__ == '__main__':
    provided = [
        "One",
        "oNE",
        "supercalifragilisticexpialidocious",
        "t",
        "aAaA",
        "Zap!",
        "Tr!ck3d y4!",
        "G0t it!"
    ]

    # For each word in the provided list, give the word to the function score word and print some fancy formatted output
    for word in provided:
        print(f"The score of {word} is: {scoreWord(word)}")
