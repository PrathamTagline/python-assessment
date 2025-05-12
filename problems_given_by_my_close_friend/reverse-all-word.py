long_string  = "hello my name is pratham patel"
reversed_word_string = "".join(word[::-1] + " " for word in long_string.split())
print(reversed_word_string)