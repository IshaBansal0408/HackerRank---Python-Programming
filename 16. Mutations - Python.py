"""Problem 16: Read a given string,change the character at a given index
                and then print the modified string.
"""
def mutate_string(string, position, character):
    str=""
    for i in range(len(string)):
        if(i==position):
            str=str+character
            continue
        str=str+string[i]
    return str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
