print("=========== ProdBug : Function ==========")
def sum(a,b):
   c = a + b
   return c

result = sum(10,20)
print ('sum is:', result)


print("=========== ProdBug : Function : Pass By Reference ==========")
def changeMe( myList ):
   myList[0] = 100;   #updated
   return

myList = [10,20,30];
print (myList)
changeMe(myList);    # Call changeMe function
print (myList)      # original list also changed



print("\n=========== ProdBug : Default Arg ==========")
def defaultArg( name, age = 18 ):
   print ("Name: ", name)
   print ("Age ", age)
   return;

defaultArg( name="Prod", age=30 )
defaultArg( name="Bug" )
