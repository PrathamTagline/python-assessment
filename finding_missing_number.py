given_list = [1,2,3,4,6,7]

def finding_missing_number(givenList):
    full_range_list = [number for number in range(1,given_list[-1])]
    given_list_in_set = set(given_list)
    full_range_list_in_set = set(full_range_list)
    missing_number = (full_range_list_in_set - given_list_in_set)
    return missing_number

print(finding_missing_number(given_list)) 
