def DisplayMenu():
    print("Welcome To Data Levearage Data Conversion Software")
    print("**************************************************")

    #Taking user info
    print(input("Enter Your Name" ))
    print(input("Enter Your Age"))

    #Temperature conversion
    print("1. celsius_conversion")
    print("2. fahreinheit_conversion")
    print("Exit")

def celsius_conversion(fahreinheit):
    return(fahreinheit-32)*5/9

def fahreinheit_conversion(celsius):
    return(celsius*9/5)+32

DisplayMenu()
choice = (input("Select ( 1-3): "))
if choice !=3:
    fahreinheit = float(input("Enter temperature value: "))
    celsius = float(input("Enter temperature value: "))
if choice == 1:
    print(f"The Temperature is (celsius_conversion{fahreinheit})")
elif choice == 2:
    print(f"The Temperature is (fahreinheit_conversion {celsius}")
elif choice == 3:
    print("Exit")
else:
    print("Please enter a valid selection.")

c = (input("Do you want to continue? (Y/N): "))

while(c == 'y' or c=='Y'):
    DisplayMenu()
choice = (input("Select ( 1-3): "))
if (choice != 3):
    fahreinheit = float(input("Enter temperature value: "))
    celsius = float(input("Enter temperature value: "))
if choice == 1:
    print(f"The Temperature is (celsius_conversion{fahreinheit})")
elif choice == 2:
    print(f"The Temperature is (fahreinheit_conversion {celsius}")
elif choice == 3:
    print("Exit")
else:
    print("Please enter a valid selection.")

c = (input("Do you want to continue? (Y/N): "))