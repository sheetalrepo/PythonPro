

print("\n=========== ProdBug : List ==========")
#List : Can contains any data types, can be modified, contains [] bracket
list1 = ['a','b','c', 10, 20]
list2 = ['apple', 'mango']
print (list1)           # It will prints complete list
print (list1[0])         # It will prints first element of the list
print (list1 + list2)   # It will prints concatenated lists
list1[0] = 30          # Possible to update
print (list1)




print("\n=========== ProdBug : Unpack List ==========")
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


print("\n=========== ProdBug : Tuples ==========")
#Tuples : Can contains any data types, Can NOT be modified (Read Only Lists), contains () bracket
tuple1 = ('a','b','c', 10, 20)
tuple2 = ('apple', 'mango')
print (tuple1)           # It will prints complete list
print (tuple1[0])         # It will prints first element of the list
print (tuple1 + tuple2)   # It will prints concatenated lists
#tuple1[0] = 30          # Possible to update



print("\n=========== ProdBug : Dictionary ==========")
# Can contain any Data Types, Can be Modified, Contains {}
dict1 = {'id': 123,'name':'sheetal', 'dept': 'automation'}
dict1[4]= 4

print (dict1)
print (dict1.keys())
print (dict1.values())
