def login(userName, password):
    while True:
        u_name = input("User name: ")
        pwd = input("Password: ")
        if u_name == userName and pwd == password:
            print("Login Successful!")
            return True
        else:
            print("Incorrect Username/Password!")
            e = input("Press 'x' to exit or any other key to try again...")
            if e == 'x':
                print("Thanks for visiting Royal Bank!")
                return False

def deposit(balance):
    amount = int(input("Enter the amount you want to deposit: "))
    balance += amount
    print("Amount Deposited Successfully!")
    return balance

def withdraw(balance):
    amount = int(input("Enter the amount you want to withdraw: "))
    if balance - amount < 10000:
        print("Insufficient Balance! Please try with smaller amount...")
        return balance
    else:
        balance -= amount
        print("Amount withdrew successfully!")
        return balance

def checkBalance(balance):
    print("Your current balance is:", balance)


print("#" * 100)
print("#" + "Welcome to Royal Kids Bank!".center(98) + "#")
print("#" * 100)
print("Please chose your user name & password to open new account:")
userName = input("Username: ")
password = input("Password: ")
print("Congratulations! Account created successfully!")
balance = 25000
print("Your opening balance is:", balance)
print("Please login by entering same username & password to perform any operation...")
if login(userName, password):
    while True:
        print("Press 1 to Deposit")
        print("Press 2 to Withdraw")
        print("Press 3 to Check Balance")
        print("Press 4 to exit")
        choice = int(input())
        if choice == 1:
            balance = deposit(balance)
            print("Your updated balance is:", balance)

        elif choice == 2:
            balance = withdraw(balance)
            print("Your updated balance is:", balance)

        elif choice == 3:
            checkBalance(balance)

        elif choice == 4:
            break

        else:
            print("Invalid Operation! Please try again...")