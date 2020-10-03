def cat(args):
    """concatenate files and print on the standard output"""
    # for every file, attempt to open, read every line, and print
    for argument in args[2:]:
        file = open(argument)
        lines = file.readlines()
        for line in lines:
            print(line, end="")
        file.close()



def tac(args):
    """concatenate and print files in reverse"""
    # same as cat, just reverse file ordering of lines
    for argument in args[2:]:
        file = open(argument)
        lines = reversed(file.readlines())
        for line in lines:
            print(line, end="")
        file.close()