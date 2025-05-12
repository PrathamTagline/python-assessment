numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

# fucntion use for the list operations
def list_operations(argument, tempList):
    match argument:
        # return length of the list
        case 1:
            return len(tempList)

        # return first three elements of the list 
        case 2:
            if len(tempList) >= 3:
                return tempList[:3]
            else:
                return "Error: The list has fewer than 3 elements."  # raise the error if the message if length of the list in blow to the 3

        # return sum of the odd numbers 
        case 3:
            odd_numbers = [item for item in tempList if item % 2 != 0]
            return sum(odd_numbers)

        #  return the list which contain the number which is duplicate in the list 
        # use the dic for the count the total duplicarte number 
        case 4:
            number_dictonary = {}
            count = 0
            for number in tempList:
                if number in number_dictonary:
                    number_dictonary[number] += 1
                else:
                    number_dictonary[number] = 1

            for key,value in number_dictonary.items():
                if number_dictonary[key] > 1 :
                    count += 1  

            return count
        
        # return the list without duplication 
        case 5:
            return list(set(tempList))

        # return message if user enter the invalid argument
        case _:
            return "Invalid selection. Please select a valid operation number."


while True:
   
    operation_number = int(input("""
1. Length of the list
2. Retrieve first 3 numbers
3. Sum of odd numbers
4. Duplicate numbers
5. List without duplication
6. stop iteration
                                     
Select the operation number: """))
        
        # if the operation 1 to 5 
    if operation_number != 6:
        result = list_operations(operation_number, numbers)
        print("Result:", result)
        # if user select the  operation 6 its stop the loop
        
    
    else:
        break 


# 