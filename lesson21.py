try:
    quit_string = "Y"
    quit_answer = "N"
    
    while quit_string != quit_answer:
        inp = float(input("please enter first number \n"))
        inp2 = float(input("please enter second number \n"))
        inp3 = input("please enter a mathematical operation: ")

        if inp3 == "*":
            print(inp*inp2)
        elif inp3 == "/":
            print(inp/inp2)
        elif inp3 =="+":
            print(inp+inp2)
        elif inp3 == "-":
            print(inp-inp2)
        else:
            print("somthing went wrong")
        quit_answer = input("do you want to exit? Y/N \n")


except ValueError as ex:
    print(ex)
except ZeroDivisionError as ex:
    print(ex)