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
    for char in vowel_string:
        if char not in vowel_counts:
            vowel_counts[char] = 1
        else:
            vowel_counts[char] += 1
    return vowel_counts

def consonants_count(string):
    consonant_counts = {}
    consonants_string = "".join(filter(remove_all_vowel, string)).lower()
    for char in consonants_string:
        if char not in consonant_counts:
            consonant_counts[char] = 1
        else:
            consonant_counts[char] += 1
    return consonant_counts


long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."
print(f"vowel count :  \n{vowel_count(long_string)}")
print()
print(f"consonants count count :  \n{consonants_count(long_string)}")