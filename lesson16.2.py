def rg():
#    file = open("rg.super.txt$$£","rt")
    with open("rg.super.txt$$£","rt") as file:
        gorf = file.read()
        print(gorf)
        if gorf == "hello":
            return "hi"
        if gorf == "hallo":
            return "guten tag"
        if gorf == "how":
            return "YOU HAVE PASSED THE TEST"
        else:
            return "bye"
    
print(rg())