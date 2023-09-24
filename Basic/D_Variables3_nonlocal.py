print("\n=========== ProdBug : Global, Local Variable  ==========")

str = "alpha"                      #global
def outerFunc():
    str = "beta"                   #inside outer func
    def innerFunc():
        str = "gamma"               #local
        print("inner: ", str)

    innerFunc()
    print("outer: ", str)

outerFunc()
print ("global: ", str)



print("\n=========== ProdBug : Global, Non local Variable  ==========")

str = "alpha"      # global
def outerFunc():
    str = "beta"         #inside outer func
    def innerFunc():
        nonlocal str       #non local i.e. accessing outer variable 
        str = "gamma"
        print("inner: ", str)

    innerFunc()
    print("outer: ", str)

outerFunc()
print ("global: ", str)