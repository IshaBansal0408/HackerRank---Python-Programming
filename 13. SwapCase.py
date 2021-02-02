def swap_case(s):
    str=""
    for i in s:
        if(i.isupper()):
            str=str+i.lower()
        elif(i.islower()):
            str=str+i.upper()
        else:
            str=str+i
    return str
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
