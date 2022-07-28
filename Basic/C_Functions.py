print("=========== ProdBug : Function : Pass By Reference ==========")

def printMe( myList ):
   myList[0] = 100;   #updated
   return

# Now you can call changeme function
myList = [10,20,30];
print myList
printMe(myList);
print myList      # original list also changed



print("\n=========== ProdBug : Default Arg ==========")
def defaultArg( name, age = 18 ):
   print "Name: ", name
   print "Age ", age
   return;

defaultArg( name="Prod", age=30 )
defaultArg( name="Bug" )
