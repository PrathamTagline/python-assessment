def prime_number(number):
    for i in range(2,number//2):
        if number % i == 0:
            return False
    return True

print(prime_number(67))