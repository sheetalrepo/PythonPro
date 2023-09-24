'''
Multi line comment
Multi line comment
Multi line comment
Multi line comment
Multi line comment

'''


#To run code
# python A_Basics.py
# python3 A_Basics.py    : It will give error and ask to put () around print stmt

print("=========== ProdBug : Hello World==========")
print ("Hello World ...")


print("\n=========== ProdBug : String ==========")
str1 = "Python"
print (">>>"+str1)          # It will prints complete string
print (str1[0])       # It will prints first character of the string
print (str1[2:5])     # It will prints characters starting from 3rd to 5th
print (str1 * 2)      # It will prints string two times
print (str1 + " World")  # It will prints concatenated string



print("\n=========== ProdBug : Int, String, Casting ==========")
x = 5
y = "John"
print(x)
print(y)

a = str(3)    # a will be "3"
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0
print(a)
print(b)
print(c)


print("\n=========== ProdBug : Naming: alphaNumeric, case sensitive and underscore allowed ==========")
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"



print("\n=========== ProdBug : Assign Mutiple Values ==========")
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)


print("\n=========== ProdBug : + , inside print ==========")
x, y = "Bat", "Ball"
print(x, y)       # Concatenation with Space
print(x + y)      # Concatenation w/o space


# Good to use comma all the time
x = 5
y = "John"
# print(x + y)  # error
print(x, y)