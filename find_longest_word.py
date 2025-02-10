long_string = "the quickdsasdadasdsda brown fox jump over the lazy dog"
word_list = long_string.split(" ")


longest_word_length = -1
lonest_word = word_list[0]

for i in word_list:
    if longest_word_length < len(i):
            lonest_word = i
            longest_word_length = len(i)

print(lonest_word)

