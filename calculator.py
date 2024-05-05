def Authentication():
    print("Login")
    input_user_name=(input("Enter user name: "))
    input_password=(input("Enter password: "))
    if (input_user_name == "admin" and input_password == "password"):
        print("Access granted")
    else:
        print("Access Denied!")
    while(input_user_name != "admin" or input_password != "password"):
        input_user_name=(input("Enter user name: "))
        input_password=(input("Enter password: "))
        if (input_user_name == "admin" and input_password == "password"):
            print("Access granted")
        else:
            print("Access Denied!")


def DisplayMenu():

    print("DATA LEAVERAGE ARITHMETIC COMPUTATION SOFTWARE")
    print("********************************************************")
    print("1. Average")
    print("2. Multiplication")
    print("3. Division")
    print("4. Maximum") 
    print("5. Exit")
    

def average(firstnum, secondnum):
    return (firstnum + secondnum) / 2
def product(num1, num2):
    return num1 * num2

def division(fnum, snum):
    return(fnum / snum)


def maximum(firstnum, secondnum):
    if (firstnum > secondnum):
        print("Maximum: ", firstnum)
    else:
        print("Maximum: ",secondnum)

Authentication()
DisplayMenu()
choice = int(input("Select Option (1-5): "))
if (choice != 5):
    fnum = float(input("Enter first number: "))
    snum = float(input("Enter second number: "))
if choice == 1:
    print(f"The Average is {average(fnum, snum)}")
elif choice == 2:
    print(f"The Product is {product(fnum, snum)}")
elif choice == 3:
    print(f"The Quotient is {division(fnum, snum)}")
elif choice == 4:
    print(f"The Maximum is: {maximum(fnum, snum)}")
elif choice == 5:
    print("Exit")
else:
    print("Please enter a valid selection.")
    
c = (input("do you want to continue? (Y/N): "))

c = (input("do you want to continue? (Y/N): "))

while(c == 'y' or c=='Y'):
    Authentication()
    DisplayMenu()
    choice = int(input("Select Option (1-5): "))
    fnum = float(input("Enter first number: "))
    snum = float(input("Enter second number: "))
    if choice == 1:
        print(f"The Average is {average(fnum, snum)}")
    elif choice == 2:
        print(f"The Product is {product(fnum, snum)}")
    elif choice == 3:
        print(f"The Quotient is {division(fnum, snum)}")
    elif choice == 4:
        print(f"The Maximum is: {maximum(fnum, snum)}")
    elif choice == 5:
        print("Exit")
    else:
        print("Please enter a valid selection.")
    c = (input("do you want to continue? (Y/N): "))

    