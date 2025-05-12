import string

VOWEL = ["a", "e", "i", "o", "u",]
CONSONANTS = [char for char in list(string.ascii_lowercase) if char not in VOWEL]


def count_vowel_and_consonants(string):
    vowel_dictionary = {}
    consonants_dictionary = {}
    for char in string:
        if char in VOWEL:
            if char not in vowel_dictionary:
                vowel_dictionary[char] = 1
            else:
                vowel_dictionary[char] += 1

        elif char in CONSONANTS:
            if char not in consonants_dictionary:
                consonants_dictionary[char] = 1
            else:
                consonants_dictionary[char] += 1    
        else:
            continue
    return vowel_dictionary, consonants_dictionary


long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."
vowel_frequency, consonant_frequency = count_vowel_and_consonants(long_string)

print(f"vowel count :  \n{vowel_frequency}")
print()
print(f"consonants count count :  \n{consonant_frequency}")