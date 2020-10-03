def cut(args):
    """remove sections from each line of files"""
    # recognize option
    if args[2] == '-f':
        files = args[4:]
        # sort values given, order priority given to natural order
        value = args[3].split(",")
        value.sort()
        for file in files:
            file = open(file)
            lines = file.readlines()
            for line in lines:
                # strip \n element from line
                line = line.rstrip("\n").split(",")
                for v in value:
                    # over extended value, print empty value
                    if int(v) > len(line):
                        print()
                    # value exists
                    else:
                        # either only column or end of table, dont print comma
                        if len(value) == 1:
                            print(line[int(v) - 1], end="")
                        else:
                            print(line[int(v) - 1], end="")
                        if v != value[-1]:
                            print(",", end="")
                print("")
            file.close()

    else:
        # default first column to print
        files = args[2:]
        for file in files:
            file = open(file)
            lines = file.readlines()
            for line in lines:
                line = line.split(",")
                print(line[0])
            file.close()




def paste(args):
    """merge lines of files"""
    files = args[2:]
    output = []
    # add all lines to array
    for i in range(len(files)):
        file = open(files[i])
        lines = file.readlines()
        output.append(lines)
        file.close()
    # reverse to output in correct order
    for i in range(len(output)):
        output[i].reverse()
    # find maximum length of column
    list_lengths = [len(i) for i in output]
    max_length = max(list_lengths)
    # print column
    for i in range(max_length):
        for k in range(len(output)):
            if len(output[k]) > 0:
                element = output[k].pop().rstrip("\n")
                if k != len(output) - 1:
                    print(element + ",", end="")
                else:
                    print(element, end="")
            else:
                if k != len(output) - 1:
                    print(",", end="")

        print()