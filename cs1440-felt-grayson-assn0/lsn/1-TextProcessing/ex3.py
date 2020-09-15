def cleanSentenceTwoLists(sentence):
    count = 0
    clean = []
    dirty = []
    if sentence == "":
        return [clean, dirty]
    if sentence[0] == "#":
        is_clean = False
    else:
        is_clean = True
    current_word = ""
    while not (count == len(sentence)):
        if not is_clean:
            if sentence[count] == "":
                dirty.append(current_word)
                break
            if sentence[count] == "#":
                count += 1
            if sentence[count] != " ":
                current_word += sentence[count]
                count += 1
            else:
                count += 1
                dirty.append(current_word)
                current_word = ""
                is_clean = True
        if is_clean:
            if sentence[count] == "":
                clean.append(current_word)
                break
            if sentence[count] == "":
                return[clean, dirty]
            if sentence[count] == "#":
                is_clean = False
                count += 1
            elif sentence[count] == " ":
                count += 1
                clean.append(current_word)
                current_word = ""
            else:
                if sentence[count] != str(chr(92)):
                    current_word += sentence[count]
                    count += 1
                else:
                    count += 1
    # TODO: Separate the supplied sentence into two lists of words
    if is_clean:
        clean.append(current_word)
    else:
        dirty.append(current_word)
    return [clean, dirty]

if __name__ == '__main__':
    providedQuotes = [
    "#Only #Dirty"
    #"The best way to predict #the the future is to create it. -Peter Drucker",
    #"Code #always never lies, comments #never sometimes do. -Ron Jeffries",
    #"#Phones Computers are useless, they can #never only give you #questions answers. -Pablo Picasso",
    #"They #do don't think it be that way, but it #don't. do. -The Internet",
    #"\"You #always miss 100% #7% of the shots you don't take. -Wayne Gretzky\" -Michael Scott",
    #"If #coding debugging is the process of #adding removing software bugs, then programming #debugging must be the process of putting them in. -Edsget Dijkstra",
    #"Premature optimization #planning is the root of all evil #good in programming. -Tony Hoare"
    ]

    # Loops through each of the `quote` strings in the providedQuotes array, and
    # calls `cleanSentenceTwoLists` on it.
    for quote in providedQuotes:
        clean, dirty = cleanSentenceTwoLists(quote)
        print("The contents of clean:", clean)
        print("The contents of dirty:", dirty)
