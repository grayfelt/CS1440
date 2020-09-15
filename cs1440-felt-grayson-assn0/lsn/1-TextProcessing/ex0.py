def findWords(sentence):
    wordsToReturn = []
    # TODO: Return the words in `sentence` that are five characters or less
    # for word in sentence...
    word = ''
    for w in sentence:
        sum = 0
        for c in w:
            sum += 1
        if sum <= 5:
            wordsToReturn.append(w)
    return wordsToReturn


if __name__ == '__main__':

    provided = [
        "Craftsman",
        "Keep",
        "Reveal",
        "personal",
        "it",
        "harmful",
        "engine",
        "short",
        "friendly",
        "killer",
        "honest",
        "season",
        "and",
        "camera",
        "strange",
        "hiccup",
        "horseshoe",
        "sphere",
        "charismatic",
        "ceiling",
        "sweet",
        "formation",
        "substitute"
        "daughter",
        "perfect"
    ]

    words = findWords(provided)
    # Prints the `words` list formatted like a sentence.
    for i in range(len(words)):
        if i != (len(words) - 1):
            print(words[i], end=" ")
        else:
            print(words[i] + "!")
