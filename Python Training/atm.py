# Global variable to store balance
"""
balance = 1000


def menu():
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        choice = int(input("Enter your Choice between 1 to 3: "))
        if choice == 1:
            print("Available balance is:", check_bal())
        elif choice == 2:
            print("Available balance after withdrawal is:", withdraw())
        elif choice == 3:
            print("Available balance after deposit is:", deposit())
        else:
            print("Invalid choice. Please choose between 1 to 3.")

        if not proceed_again():
            print("Thank You...")
            break


def check_bal():
    global balance
    return balance


def withdraw():
    global balance
    w_amt = int(input("Enter an Amount to withdraw: "))
    if w_amt <= balance:
        balance -= w_amt
        return balance
    else:
        return "Insufficient Balance"


def deposit():
    global balance
    d_amt = int(input("Enter an Amount to deposit: "))
    balance += d_amt
    return balance


def proceed_again():
    n = input("Do you want to proceed again? (y/n): ")
    return n.lower() == 'y'


# Main execution
def main():
    n = int(input("Enter your PIN: "))
    if n == 123:
        menu()
    else:
        print("OOPS!! Enter a Correct PIN")


if __name__ == "__main__":
    main()


for i in range(1,10):
    if (i%2==0):
        pass
    else:
        print(i)
    print("YES")

"""

