from calculator import add, subtract, multiply, divide, clear

print("Quick Calc")

while True:

    print("\nChoose operation")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Clear")
    print("6 Exit")

    choice = input("Choice: ")

    if choice == "6":
        break

    if choice == "5":
        print(clear())
        continue

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if choice == "1":
        print(add(a,b))

    elif choice == "2":
        print(subtract(a,b))

    elif choice == "3":
        print(multiply(a,b))

    elif choice == "4":
        print(divide(a,b))