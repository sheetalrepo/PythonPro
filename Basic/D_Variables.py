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

