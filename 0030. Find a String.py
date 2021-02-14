def count_substring(string, sub_string):
    occ_count=0
    for i in range(len(string)):
        if(string[i:i+len(sub_string)]==sub_string):
            occ_count+=1
    return occ_count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
