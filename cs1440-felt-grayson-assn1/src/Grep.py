def grep(args):
    """print lines that match patterns"""
    # that do not include:
    if args[2] == '-v':
        index = args[3]
        for element in args[4:]:
            file = open(element)
            lines = file.readlines()
            for line in lines:
                # only real difference between two conditions
                if index not in line:
                    print(line, end="")
            file.close()
    # that include:
    else:
        # what we are looking for
        index = args[2]
        for element in args[3:]:
            file = open(element)
            lines = file.readlines()
            for line in lines:
                # print every occurrence of index
                if index in line:
                    print(line, end="")
            file.close()
