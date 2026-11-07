def dahboard() -> None:
    print("--------- Welcome ----------")
    print("Hello! dear users welcome to this number guessing game you can proceed with following options by pressing respective number")
    print("1.start new game")
    try:
      choice =   int(input("select an option:"))
    except ValueError:
        print("Please enter the valid number!")
        return
    match choice:
        case 1:
            print("starting game")
        case _:
            print("invalid option")

dahboard()
