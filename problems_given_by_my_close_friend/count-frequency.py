from string import punctuation

long_string = "this is a test,test is a test,"
filtered_string = "".join(" " if c in punctuation else c for c in long_string).strip()

word_list = filtered_string.split(" ")
unique_word = set(word_list)
frequence_counts = {}

for i in unique_word:
    count = word_list.count(i)
    frequence_counts[i] = count

print(frequence_counts)





