def f (frog):
    print(frog)
    if frog < 5:
         return 
    frog = frog - 1

    f(frog)


f(8)