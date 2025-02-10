def prime_number(number):
    for i in range(2,number):
        if number % i == 0:
            return True
    return False

print(prime_number(22))