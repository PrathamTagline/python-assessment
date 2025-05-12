def count_frequency_of_character(givenString):
    lowercase_string = givenString.lower()
    frequence_dictionary = {}
    for char in lowercase_string:
        if char not in frequence_dictionary:
            frequence_dictionary[char] = 1
        else:
            frequence_dictionary[char] += 1

    return frequence_dictionary

long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."
all_characters_frequency = count_frequency_of_character(long_string)
print(f"frequency of all characters : \n {all_characters_frequency}")
