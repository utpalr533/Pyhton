a=int(input("Enter a number:   "))
match a:
    case 122:
        print("the value is 122")
    case 3:
        print("the value is 3")
    case 4:
        print("the value is 4")

    case _:    
        print("better luck next time")