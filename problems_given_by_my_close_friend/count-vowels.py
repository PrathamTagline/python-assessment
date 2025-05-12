
long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."

def remove_all_consonant(char):
    vowels = ["a","e","i","o","u",]
    return char.lower() in vowels

filtered_string = "".join(filter(remove_all_consonant, long_string)).lower()
count_a = filtered_string.count("a")
count_e = filtered_string.count("e")
count_i = filtered_string.count("i")
count_o = filtered_string.count("o")
count_u = filtered_string.count("u")

vowel_counts = dict(a=count_a,e=count_e,i=count_i,o=count_o,u=count_u)

print(vowel_counts)