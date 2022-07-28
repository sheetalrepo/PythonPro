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
str = "Python"
print ">>>"+str          # It will prints complete string
print str[0]       # It will prints first character of the string
print str[2:5]     # It will prints characters starting from 3rd to 5th
print str * 2      # It will prints string two times
print str + " World" # It will prints concatenated string


print("\n=========== ProdBug : List ==========")
#List : Can contains any data types, can be modified, contains [] bracket
list1 = ['a','b','c', 10, 20]
list2 = ['apple', 'mango']
print list1           # It will prints complete list
print list1[0]         # It will prints first element of the list
print list1 + list2   # It will prints concatenated lists
list1[0] = 30          # Possible to update
print list1


print("\n=========== ProdBug : Tuples ==========")
#Tuples : Can contains any data types, Can NOT be modified (Read Only Lists), contains () bracket
tuple1 = ('a','b','c', 10, 20)
tuple2 = ('apple', 'mango')
print tuple1           # It will prints complete list
print tuple1[0]         # It will prints first element of the list
print tuple1 + tuple2   # It will prints concatenated lists
#tuple1[0] = 30          # Possible to update



print("\n=========== ProdBug : Dictionary ==========")
dict1 = {}
dict1['one'] = "One"
dict1[2]     = "Two"
dict2 = {'id': 123,'name':'sheetal', 'dept': 'automation'}

print dict1['one']
print dict1[2]
print dict2
print dict2.keys()
print dict2.values()
