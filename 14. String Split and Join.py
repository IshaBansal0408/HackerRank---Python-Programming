# Problem 14: Split the string on a " " (space) delimiter andjoin using a -
def split_and_join(line):
    line=line.split(" ")
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
