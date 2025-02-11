def palindrome_string(string):
    i,j = 0,len(string) - 1 
    if len(string) % 2 == 1:
        while i != j :
            if string[i] == string[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
    elif len(string) % 2 == 0:
        while i + 1 != j - 1:
            if string[i] == string[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
    return True


string = "ababa"
print(palindrome_string(string))
