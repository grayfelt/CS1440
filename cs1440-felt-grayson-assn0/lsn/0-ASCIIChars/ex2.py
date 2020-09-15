def listOfASCIIInts(charList):
    list = []
    # TODO: convert a list of characters into a list of ints based on ASCII
    # Reference: https://www.w3resource.com/python-exercises/python-basic-exercise-144.php
    if isinstance(charList, str):
        length = len(charList)
        if length == 0:
            return list
        for i in range(length):
            list.append(int(ord(charList[i])))
    else:
        if len(charList) == 0:
            return list
        else:
            for a in charList:
                list.append(int(ord(a)))

    return list


if __name__ == '__main__':
    provided = ["A", "B", "c", "1", "-", "_", "~", " ", "z", "Y", "x"]
    provided2 = "Will you pass this test too?"

    print(listOfASCIIInts(provided))
    print(listOfASCIIInts(provided2))
