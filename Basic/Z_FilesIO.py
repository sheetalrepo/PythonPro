print("=========== ProdBug : User Input ==========")

#str = raw_input("Enter your name: ")
#print "Your name is : ", str.upper()



print("\n=========== ProdBug : File  ==========")
#wb: open/create file for writing
myFile = open("readme.txt", "wb")
print "Name of the file: ", myFile.name
myFile.write('We are learning Python 3')
print('File written successfully')
myFile.close()



print("\n=========== ProdBug : Exception ==========")
#r: read access
myFile2 = open("readme.txt", "r")
try:
    myFile2.write('We are learning Python')
except IOError:
   print "Not able to write, pls check file access"
finally:
   print "I am finally block"




print("\n=========== ProdBug : Raise/Throw Exception ==========")
def votingAge( age ):
   if age < 18:
      raise Exception("Sorry, no age below 18")
   else:
      print('You can vote')


try:
    votingAge(20)
except Exception as e:
   print e
