def finding_missing_number(givenList):
    full_range_list = {number for number in range(1,given_list[-1])}
    given_list_in_set = set(given_list)
    missing_number = (full_range_list - given_list_in_set)
    return missing_number

given_list = [1,2,3,4,6,7]

print(f"missing number : {finding_missing_number(given_list)}") 
