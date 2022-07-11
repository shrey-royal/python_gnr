'''
Royal Kids Bank

Design a Banking App in Python that has the following functionalities:-
User can:-

◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.

◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions

◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.

◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.

◆CHECK BALANCE will show the latest updated balance to user.

◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
'''
print()
print("Welcome To Royal Kids Bank...".center(100, '*'))

while(True):
    print("\n1. Open A New Account")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        print("Thanks for using Royal Kids Bank")
        break
    else:
        print("Invalid Choice, Please Enter a valid choice again!")