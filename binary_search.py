def binary_search(givenNumber,numberList):

    # leading point and end point of the list ( it will change according to the following condition )
    ledingPoint,endingPoint = 0,len(numberList)

    # this 
    while ledingPoint < endingPoint:
        centerPoint = ledingPoint + (endingPoint - ledingPoint) // 2
        if numberList[centerPoint] == givenNumber:
            return (centerPoint,numberList[centerPoint])
        
        elif numberList[centerPoint] < givenNumber:
            ledingPoint = centerPoint + 1

        elif numberList[centerPoint] > givenNumber:
            endingPoint = centerPoint - 1
    
    return "element is not available in the list"


list1 = [1,2,3,4,5,6,7]
print(binary_search(-86,list1))