print("=========== ProdBug : Global variables ==========")

x = "apple"
def abc():
    print("inside:", x)   # Able to access from inside function

abc()
print("outside:", x)


print("\n=========== ProdBug : Local Variable  ==========")

def xyz():
    y = "mango"
    print("inside:", y)   # Able to access from inside function

xyz()
#print("outside:", y)   # exception



print("\n=========== ProdBug : Global and Local Variable  ==========")

m = "grapes"
def mno():
    global m                #Need to declare global in case we modifiy global var
    m = "sweet " + m
    n = "orange"
    print("inside:", n)
    print("inside:", m)   # sweet grapes

mno()



print("\n=========== ProdBug : Non local Variable  ==========")
# Need to run via python3 cmd

def outerFunc():
    str = "alpha"

    def innerFunc():
        nonlocal str
        str = "beta"
        print("inner:", str)

    innerFunc()
    print("outer:", str)


outerFunc()
