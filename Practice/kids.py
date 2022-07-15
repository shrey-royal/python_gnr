userinfo = {"uname":"password", "admin":"admin"}
# print(userinfo.keys(), "\n", userinfo.values())
# balance = 25000

def new_user(username, password):
    userinfo.update({username:password})
    print("New Account Created...")


def login(uname, password):
    for i in userinfo.keys():
        if i == uname:
            if userinfo.get(i) == password:
                return 1
            else:
                return 0

def deposit(balance):
    dep_amount = int(input("Enter the amount that you want to deposit: "))
    if dep_amount >= 20000:
        print("naa thaay")
    else:
        balance += dep_amount
        print("Your current balance is ", balance)
    
    return balance

def withdraw(balance):
    print("Your current balance is ", balance)
    withdraw_amount = int(input("Enter the amount that you want to Withdraw: "))
    if withdraw_amount >= 20000:
        print("Alya naa thaay")
    else:
        if balance - withdraw_amount <= 25000:
            print("not possible")
        else:
            balance -= withdraw_amount
            print("Your current balance is ", balance)

    return balance
    
def check_balance(balance):
    print("Your current balance is ", balance)
    return balance

print("\n")
print("Welcome To Royal Kids Bank".center(100, '*'))

while(True):
    balance = 25000
    print("\n1. Open A New Account")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username: ")
        pswd = input("Enter password: ")
        new_user(username, pswd)
        print("Your initial balance is ", balance)

    elif choice == 2:
        username = input("Enter username: ")
        pswd = input("Enter password: ")
        if login(username, pswd) == 1:
            print("User Logged In...")
            
            while(True):
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. View Balance")
                print("4. Logout")
                inner_choice = int(input("Enter your choice: "))

                if inner_choice == 1:
                    print("Deposit Money...")
                    balance = deposit(balance)
                    
                elif inner_choice == 2:
                    print("Withdraw amount...")
                    balance = withdraw(balance)
                    
                elif inner_choice == 3:
                    print("View Account Balance")
                    check_balance(balance)
                    
                elif inner_choice == 4:
                    print("Logging Out...")
                    break
                else:
                    print("Invalid Choice, Please Enter a valid choice again!")

        else:
            print("Incorrect Username or Password...")
            choice = input("Press X to exit or press any other key to try again...\n > ")
            if choice == 'X' or choice == 'x':
                print("Thanks for visiting our Bank...")
                break

    elif choice == 3:
        print("Thanks for using Royal Kids Bank")
        break
    else:
        print("Invalid Choice, Please Enter a valid choice again!") 



'''

deposit > 50k not possible
withdraw < 10k -> not possible
view balance -> balance

'''