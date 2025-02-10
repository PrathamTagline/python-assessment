import string 

def count_frequency_of_character(givenString):
    all_lowercase_letters = list(string.ascii_lowercase)
    lowercase_string = givenString.lower()
    frequence_dictionary = {}
    for char in all_lowercase_letters:
        frequence = lowercase_string.count(char)
        if frequence == 0:
            continue
        else:
            frequence_dictionary[char] = frequence

    return frequence_dictionary

long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."
a = count_frequency_of_character(long_string)
print(a)
