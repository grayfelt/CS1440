def cleanSentence(sentence):
    result = []
    if sentence == "":
        return result
    # TODO: Add the words *not* starting with `#` to the 'result' list
    if sentence[0] == "#":
        word = False
    else:
        word = True
    count = 0
    current_word = ""
    while not (count == len(sentence)):
        if not word:
            if sentence[count] != " ":
                count += 1
            else:
                count += 1
                word = True
        if word:
            if sentence[count] == "#":
                word = False
                count += 1
            elif sentence[count] == " ":
                count += 1
                result.append(current_word)
                current_word = ""
            else:
                if sentence[count] != str(chr(92)):
                    current_word += sentence[count]
                    count += 1
                else:
                    count += 1
    if current_word != "":
        result.append(current_word)
    return result

if __name__ == '__main__':
    providedQuotes = [
    "The best way to predict #the the future is to create it. -Peter Drucker",
    "Code #always never lies, comments #never sometimes do. -Ron Jeffries",
    "#Phones Computers are useless, they can #never only give you #questions answers. -Pablo Picasso",
    "They #do don't think it be that way, but it #don't. do. -The Internet",
    "\"You #always miss 100% #7% of the shots you don't take. -Wayne Gretzky\" -Michael Scott",
    "If #coding debugging is the process of #adding removing software bugs, then programming #debugging must be the process of putting them in. -Edsget Dijkstra",
    "Premature optimization #planning is the root of all evil #good in programming. -Tony Hoare"
    ]

    # Loops through each of the `quote` strings in the providedQuotes array, and
    # calls `cleanQuote` on it.
    for quote in providedQuotes:
        print(cleanSentence(quote))
