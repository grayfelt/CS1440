import os

def concatenate(file):
    '''
    Prints the contents of a text file line by line, from the beginning. Similar to the `cat` command in the shell. File is an opened file wit h write permissions. This tool does *not* close a file when it is finished.
    '''
    file.seek(0)
    return file.read()


def printContentsOfFile(fileName):
    # TODO:
    # 0) Open the file
    fileObj = open(fileName)
    # 1) Give the file to the `concatenate` function
    print(concatenate(fileObj))
    # 2) Close the file
    fileObj.close()

if __name__ == '__main__':
    # `os.getcwd()` returns the (C)urrent (W)orking (D)irectory as a string.
    # Synonymous to `pwd` in the shell
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    fileName = input("File Path: ")
    printContentsOfFile(fileName)
