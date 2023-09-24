
print("=========== ProdBug : If Else ==========")
a = 100
b = 200
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")


# No bracket after if() 
print("=========== ProdBug : If Elif Else==========")
a = 10
b = 20
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



print("\n=========== ProdBug : While/Break ==========")
count = 0
while count < 10:
    print ('Count is:', count)
    count = count + 1
    if count == 5:
        break


print("\n=========== ProdBug : For Loop ==========")
fruitList = ['orange', 'apple',  'mango']
for f in fruitList:
    print ('Fruit :', f)

#char can be iterated
for a in 'World':
    print ('Current Letter :', a)