n = int(input("Enter a number (1-4): "))

match n:
    case 1:
        print("Summer")
    case 2:
        print("Monsoon")
    case 3:
        print("Winter")
    case 4:
        print("Spring")
    case _:
        print("Invalid number")