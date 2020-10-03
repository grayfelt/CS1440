def sort(args):
    """sort lines of text files"""
    # dependant on built-in sort() method
    lines = []
    for element in args[2:]:
        # grab every line
        file = open(element)
        new_lines = (file.readlines())
        for line in new_lines:
            lines.append(line)
        file.close()
    # sort and print
    lines.sort()
    for line in lines:
        print(line, end="")


