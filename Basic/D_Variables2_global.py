print("\n=========== ProdBug : Global and Local Variable  ==========")
g1 = "apple"
def mno():
    g1 = "mango"  # g is local variable here not global
    print("local g:", g1)  #mango

print("Before:", g1)   # apple
mno()
print("After:", g1)   #apple


print("\n=========== ProdBug : Global and Global Variable  ==========")
g2 = "bat"
def mno():
    global g2     # g become global inside func
    g2 = "ball"  # g is global variable here not local
    print("global g:", g2)  #apple

print("Before:", g2)   # apple
mno()
print("After:", g2)   #apple

