from string import punctuation

sentence = ["My name is Ram","He is a good person","You should be careful while coding","He can do better","The person is mysterious","Jay Shree Ram","It is my pen."]


def split_word_in_list(sentences):
    splited_word_by_sentence = []
    for sentence in sentences:
        filtered_string = "".join(" " if c in punctuation else c for c in sentence).strip()
        word_list = filtered_string.split(" ")
        splited_word_by_sentence.append(word_list)

    return splited_word_by_sentence

def frequence_of_word_map(sentence):
    frequence_counts = {}
    splited_sentence = split_word_in_list(sentence)
    for i in splited_sentence:
        for j in i:
            if j not in frequence_counts:
                frequence_counts[j] = 1
            else:
                frequence_counts[j] += 1
    return frequence_counts
    

word_count = frequence_of_word_map(sentence) 
print(word_count)

