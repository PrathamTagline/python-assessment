class BankAccount:

    def __init__(self, name, accNumber, balance, pin):
        self.name = name
        self.accNumber = accNumber
        self.balance = balance
        self.__pin = pin

    def getUserDetails(self):
        accNumber = input("Enter Your Account number : ")
        pin = input("Enter Your PIN : ")
        print("")
        try:
            assert int(accNumber) == self.accNumber and pin == self.__pin
            print(f"account holder name : {self.name}".title())
            print(f"account number : {self.accNumber}".title())
            print(f"current balance : {self.balance}".title())

        except AssertionError:
            print("account number or pin wrong plz try again")

    def depositMoney(self):
        accNumber = input("Enter Your Account number : ")
        pin = input("Enter Your PIN : ")
        print("")
        try:
            assert int(accNumber) == self.accNumber and pin == self.__pin
            print(f"current balance : {self.balance}".title())
            print("")
            depositAmount = int(input("enter deposit amount : ".title()))
            self.balance += depositAmount
            print(
                f"current balance after the deposit money : {self.balance}".title())

        except AssertionError:
            print("account number or pin is not match plz try again".title())

    def withdrawMoney(self):
        accNumber = input("Enter Your Account number : ")
        pin = input("Enter Your PIN : ")
        print("")
        try:
            if int(accNumber) == self.accNumber and pin == self.__pin:

                withdrawAmount = int(input("enter withdraw amount : ".title()))

                try:
                    assert self.balance > withdrawAmount
                    self.balance -= withdrawAmount
                    print(
                        f"current balance after the withdraw money : {self.balance}".title())

                except AssertionError:
                    print("Your account don't have sufficient balance")
        except:
            print("account number or pin is not match plz try again".title())


a = BankAccount("pratham", 123456, 20000, "patel112233")

while True:

    operation = int(input("""
                          
1. Get User Details 
2. Deposit Money
3. Withdraw Money
4. break loop
                                     
Select the operation number: """))
    print("")
    match operation:

        case 1:
            a.getUserDetails()

        case 2:
            a.depositMoney()

        case 3:
            a.withdrawMoney()

        case 4:
            break
