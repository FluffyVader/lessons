def rg():
    file = open("rg.super.txt$$£","rt")
    gorf = file.read()
    print(gorf)
    print("closed")
    file.close()
    if gorf == "hello":
        return "hi"
    if gorf == "hallo":
        return("guten tag")
    if gorf == "how":
        return"YOU HAVE PASSED THE TEST"
    else:
        return "bye"
    
print(rg())