import string
long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."
vowels = ["a","e","i","o","u",]
consonants = [char for char in list(string.ascii_lowercase) if char not in vowels]

def remove_all_vowel(char):
    return char.lower() in consonants

def remove_all_consonant(char):
    return char.lower() in vowels

vowel_string = "".join(filter(remove_all_consonant, long_string)).lower()
consonants_string = "".join(filter(remove_all_vowel, long_string)).lower()

vowel_counts = {}
consonant_counts = {}
for char in vowels:
    count = vowel_string.count(char)
    vowel_counts[f"{char}"] = count

for char in consonants:
    count = consonants_string.count(f'{char}')
    if count != 0:
        consonant_counts[f"{char}"] = count




print(vowel_counts)
print(consonant_counts)