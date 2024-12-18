def f(bebe):
    if bebe > 1000:
        return
    bebe = bebe * 2

    f(bebe)
    print(bebe)

f(2)