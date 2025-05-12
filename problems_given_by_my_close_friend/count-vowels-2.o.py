from functools import reduce
import datetime
long_string = "When we run the above program, an innovators.csv file is created in the current working directory with the given entries."
start_time = datetime.datetime.now()
count_a = reduce(lambda count, char: count + 1 if char == 'a' else count, long_string, 0)
count_e = reduce(lambda count, char: count + 1 if char == 'e' else count, long_string, 0)
count_i = reduce(lambda count, char: count + 1 if char == 'i' else count, long_string, 0)
count_o = reduce(lambda count, char: count + 1 if char == 'o' else count, long_string, 0)
count_u = reduce(lambda count, char: count + 1 if char == 'u' else count, long_string, 0)

vowel_counts = dict(a=count_a,e=count_e,i=count_i,o=count_o,u=count_u)
end_time = datetime.datetime.now()

total_time = end_time - start_time
print(total_time)
print(vowel_counts)
