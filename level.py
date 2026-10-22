n = int(input("Enter a number (1-3): "))

match n:
    case 1:
        print("Low")
    case 2:
        print("Medium")
    case 3:
        print("High")
    case _:
        print("Invalid number")