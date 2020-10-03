def wc(files):
    """print newline, word, and byte counts for each file"""
    line_total = 0
    word_total = 0
    character_total = 0
    for element in files[2:]:
        file = open(element)
        # reset count
        line_count = 0
        word_count = 0
        character_count = 0
        for line in file:
            line_count += 1
            character_count += len(line)
            word_list = line.split()
            word_count += len(word_list)
        print("%-6d %-6d %-6d %s" % (line_count, word_count, character_count, element))
        line_total += line_count
        word_total += word_count
        character_total += character_count
    if len(files) > 3:
        # for more than one file, print total
        print("%-6d %-6d %-6d %s" % (line_total, word_total, character_total, "total"))
