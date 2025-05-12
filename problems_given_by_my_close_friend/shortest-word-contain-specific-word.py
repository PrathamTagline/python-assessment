long_string = "the quick brown fox jump over the lazy dog"
word_list = long_string.split(" ")

special_character = "o"
shortest_word_length = 999
shortest_word = word_list[0]

for i in word_list:
    if shortest_word_length > len(i):
        if special_character in i:
            shortest_word = i
            shortest_word_length = len(i)

print(shortest_word)
