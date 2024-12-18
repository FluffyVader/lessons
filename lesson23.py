user_input = int(input("please enter a number\n"))
variable = 1
for i in range(user_input,0,-1):
    variable = i * variable
print(variable)