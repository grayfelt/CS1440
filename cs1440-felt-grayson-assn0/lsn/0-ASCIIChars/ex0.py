def displayASCII():
    # TODO: Display all printable ASCII characters in the range [32, 126].
    for i in range(32, 127):
        print(f"chr({i}) = {chr(i)}")

if __name__ == '__main__':
    displayASCII()
