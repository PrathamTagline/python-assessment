def logest_word_in_string(string):
    word_list = string.split(" ")
    longest_word_length = -1
    longest_word = word_list[0]

    for i in word_list:
        if longest_word_length < len(i):
                longest_word = i
                longest_word_length = len(i)
    
    return longest_word

long_string = "the quickdsasdadasdsda brown fox jump over the lazy dog"
print(logest_word_in_string(long_string))