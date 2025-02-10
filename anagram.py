origial_string = "apple"
anagram_string = "ppalep"

origial_string_list = list(origial_string)

def is_anagram(character_list,anagram_string):
    for char in anagram_string:
        if char in character_list:
            character_list.remove(char)
        else:
            return False
    return True


agagram = is_anagram(origial_string_list,anagram_string)
print(agagram)