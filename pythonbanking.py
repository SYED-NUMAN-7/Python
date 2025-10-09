#  PYHTON BANKING PROGRAM
def show_balance(balance):
    print("***********************")
    print(f"Your balance is : ${balance:.2f}")
    print("***********************")

def deposit():
    print("***********************")
    amount = float(input("Enter the amount to be deposited : "))
    print("***********************")

    if amount < 0 :
        print("***********************")
        print("The amount is not valid")
        print("***********************")
        return 0
    else :
        return amount

def withdraw(balance):
    print("***********************")
    amount = float(input("Enter the amount to be withdrawn : "))
    print("***********************")

    if amount > balance :
        print("***********************")
        print("Insufficient funds")
        print("***********************")
        return 0
    elif amount < 0 :
        print("***********************")
        print("amount can't be less than zero")
        print("***********************")
        return 0 
    else :
        return amount

def main():
    
    balance = 0
    is_running = True

    while is_running :
        print("***********************")
        print("Welcome to Banking")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("***********************")

        choice = (input("Enter (1/2/3/4) : "))

        if choice == '1' :
            show_balance(balance)
        elif choice == '2' :
            balance += deposit()
        elif choice == '3' :
            balance -= withdraw(balance)
        elif choice == '4' :
            is_running = False
        else :
            print("***********************")
            print("This is Not a Valid Choice")
            print("***********************")

if __name__ == '__main__' :
    main()

