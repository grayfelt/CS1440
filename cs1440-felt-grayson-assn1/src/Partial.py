def head(args):
    """output the first part of files"""
    # specify number of lines
    if args[2] == "-n":
        line_count = int(args[3])
        for argument in args[4:]:
            file = open(argument)
            lines = file.readlines()
            # for more than one file, specify file
            if len(args) > 5:
                print("==> " + argument + " <==")
            i = 0
            for line in lines:
                if i < line_count:
                    print(line, end="")
                i += 1
            file.close()
            print("")
    else:
        for argument in args[2:]:
            file = open(argument)
            lines = file.readlines()
            if len(args) > 3:
                print("==> " + argument + " <==")
            i = 0
            for line in lines:
                if i < 10:
                    print(line, end="")
                i += 1
            file.close()
            print("")


def tail(args):
    """output the last part of files"""
    # identical to head, just printing from behind
    if args[2] == "-n":
        line_count = int(args[3])
        for argument in args[4:]:
            output = []
            file = open(argument)
            lines = reversed(file.readlines())
            i = 0
            for line in lines:
                if i < line_count:
                    output.append(line)
                i += 1
            output.reverse()
            if len(args) > 3:
                print("==> " + argument + " <==")
            for v in output:
                print(v, end="")
            print()
            file.close()
    else:
        for argument in args[2:]:
            output = []
            file = open(argument)
            lines = reversed(file.readlines())
            i = 0
            for line in lines:
                if i < 10:
                    output.append(line)
                i += 1
            output.reverse()
            if len(args) > 3:
                print("==> " + argument + " <==")
            for v in output:
                print(v, end="")
            print()
            file.close()
