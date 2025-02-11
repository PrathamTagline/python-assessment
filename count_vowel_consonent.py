import string
VOWEL = ["a","e","i","o","u",]
CONSONANTS = [char for char in list(string.ascii_lowercase) if char not in VOWEL]

def remove_all_vowel(char):
    return char.lower() in CONSONANTS 

def remove_all_consonant(char):
    return char.lower() in VOWEL

def vowel_count(string):
    vowel_counts = {}
    vowel_string = "".join(filter(remove_all_consonant, string)).lower()
    for char in VOWEL:
        count = vowel_string.count(char)
        vowel_counts[f"{char}"] = count
    return vowel_counts

def consonants_count(string):
    consonant_counts = {}
    consonants_string = "".join(filter(remove_all_vowel, string)).lower()
    for char in CONSONANTS:
        count = consonants_string.count(f'{char}')
        if count != 0:
            consonant_counts[f"{char}"] = count
    return consonant_counts


long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."
print(vowel_count(long_string))
print(consonants_count(long_string))