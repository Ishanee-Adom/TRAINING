#converting your temperature into either celsius or fahrenheit

print("Hello! Welcome To Temprature Converter")

while True:
    print("Select conversion")
    print("Select 1 if celsius to fahrenheit")
    print("Select 2 if fahrenheit to celsius")

    choice=input("Enter choice 1 or 2  ")

    if choice==("1"):
        celsius=float(input("Enter temperature in degree celsius "))
        fahrenheit=(celsius *9/5) + 32
        print(f"Temperature of {celsius} degree celsius is {fahrenheit}")
        
    elif choice==("2"):
        fahrenheit=float(input("Enter temperature in degree fahrenheit "))
        celsius=(fahrenheit - 32) * 5/9
        print(f"Temperature of {fahrenheit} degree fahrenheit is {celsius} degree celsius")

    else:
        print("Invalid input")

    #Asking user whether they want to perform another conversion
    continuation=input("Do you want to perform another conversion Yes/No:  ")
    if continuation != "Yes":
        break


