from functools import reduce


class Numbers:

    def __init__(self, numberList):
        self.numberList = numberList

    def get(self):
        return self.numberList

    def change_original_values(self, func):
        newList = list(map(func, self.numberList))
        self.numberList = newList
        return self.numberList

    def filter_values(self, func):
        return list(filter(func, self.numberList))

    def compound_the_numbers(self, func):
        return reduce(func, self.numberList)


nums = Numbers([2, 5, 1, 66, 22, 11, 10])
print("Numbers: ",nums.get())
print("Compounded value: ",nums.compound_the_numbers(func=lambda x, y: x+y))
print("New values: ",nums.change_original_values(func=lambda x: x*2))
print("Filtered values: ",nums.filter_values(func=lambda x: (x/2) % 2 == 1))
