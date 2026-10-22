user = input("Enter True or False: ").strip().lower()

match user:
    case "true":
        print("User is active")
    case "false":
        print("User is tru")
    case _:
        print("Invalid input")