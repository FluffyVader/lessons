def compute (x):
    print(x*x/(x-2))


try:
    a = int(input("please enter a number: "))
    compute(a)
except ValueError as e:
    print("VALUE_ERROR")
    print(e)
except ZeroDivisionError as e:
    print("DIVISION_ERROR (by zero)")
    print(e)