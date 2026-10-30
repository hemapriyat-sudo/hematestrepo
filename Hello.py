print('Hema Here')
Fruit_Name = 'Orange'
print(Fruit_Name[1])
print(len(Fruit_Name))
Name = 'Hema ' + 'Priya '
print(Name)
print(Name + ' ' + str(3)) #number should be converted to string before concatenating

print('Repetition')
print(Name * 2)

print('I love {}'.format('India'))
print('I love {} {} times'.format('India', 3))

print('My first name is {}. And my last name is {}.'.format('Hemapriya', 'Thiagarajan'))
print('My first name is {:15}. And my last name is {:15}.'.format('Test', 'Hemapriya', 'Thiagarajan'))

print('*** Table ***')
print('{0:10} | {1:10}'.format('Name','Fav Color')) #default alignment left
print('{0:^10} | {1:^10}'.format('Hemapriya','Green')) #alignmnet center
print('{0:>10} | {1:>10}'.format('Raja','Blue')) #alignmnet right
print('{0:<10} | {1:<10}'.format('Shreya','Purple')) # alignment left
print('{0:10} | {1:10.2f}'.format('Riya Shoe cost',49.4509))

print('{0:10} | {1:10}'.format('Riya','Black'))
"""
fruitName = input('Enter Fruit Name: ')
print('{} is a lovely fruit.'.format(fruitName))

age = int(input('Enter your age: '))
if (age > 12 and age < 20):
    print('Teen')
elif (age <= 12):
    print('Kid')
else:
    print('adult')
print('Done')
"""
list_name = ['Hema', 32]
print(list_name[0])
list_name[0]='Priya'
print(list_name[-1]) #last item on the list
list_name.append('Raja') #add one item to the list. It appends at the end
list_name.extend(['Riya', 'Shreya']) #add more item to the list. It adds at the end
print(list_name)

#Slice - on lists
names = ['a','b','c','d','e']
someNames = names[2:4] # from index 2 till 3. Not including 4. So, 2 items.
print(someNames)
someNames = names[-2:] # from last 2 items. index starts from last before (2nd from last) item
print(someNames)
#String slice
myName = 'Hemapriya'
print(myName[0:4])

#find element in the list 
try:
    idx = names.index('z')
    print(idx) # this returns index of 'c'
except:
    print('Not found')
print('Done')

for number in someNames:
	print(number.upper())

num = 0
while(num < len(names)):
     print(names[num])
     num = num + 1

fruits = ['banana','apple','orange','guava']
sortedFruits = sorted(fruits) #returns sorted values
print(sortedFruits)  
fruits.sort() #actual object is sorted
print(fruits)


#Range
for number in range(0,4):
     print(number)

for number in range(0,4,2):
     print(number)

for number in range(0,4,3):
     print(number)

for number in range(0,len(fruits),2):
     print(fruits[number])
print('****', fruits)
print('****')
for number in range(0,len(fruits)):
     print(number)
     print(fruits[number])


#Creating dictionaries
contacts = {
	'Hema':['4846826088','9998887777'],
	'Raja':'4846858665'
}
print(contacts)

#Adding
contacts['Riya'] = '1112223333'
print(contacts)

#access by key
print(contacts['Riya'])

#removing
del contacts['Riya']
print(contacts)

#searching and Loop
for contact in contacts.keys():
     print(contact)
     print(contacts[contact])

for contact in contacts.values():
     print(contact)

for name, phone in contacts.items():
     print(name)
     print(phone)

newContacts = {
	'Hema': {
        'phone':['4846826088','9998887777'],
        'email':'hema@gmail.com'
    }
    ,
	'Raja': {
            'phone':['4846826555','2225558888'],
            'email':'raja@gmail.com'
    }
}

print('^^^^^^^^^^^^^^^^^^^^^^^'*5)
for name, contact in newContacts.items():
     print(name)
     for phn, email in contact.items():
          print(phn)
          print(email)
print('^^^^^^^^^^^^^^^^^^^^^^^'*5)

#Tuple
#create
name = ('Hema','Priya')
print(name)
name = ('Raja',)
print(name)

#delete
del name

# convert
"""
use list(x) to convert tuples to list
use tuple(x) to convert list to tuple
type(x) returns the object's type
"""
name_tuple = ('Hema','Raja','Riya','Shreya')
name_list = list(name_tuple)
print(name_tuple)
print(name_list)

name_list.append('Guest')
print(name_list)

#print object type
print(type(name_tuple))
print(type(name_list))

#iteration - same as list
for name in name_tuple:
     print(name)

# assignment - can use tuple to assign value to multiple variables
name_tuple = ('Hema','Raja')
name_list = ['Riya','Shreya']
(Mom,Dad) = name_tuple
(Elder,Younger) = name_list

print('Mom name {} and Dad name {}.'.format(Mom, Dad))
print('Elder name {} and Younger name {}.'.format(Elder, Younger))

def max_min(numberTuple):
     return (max(numberTuple),min(numberTuple))

#Inbuilt max and min functions of Tuples
numberTuple = (10,39,45,67,84,22,99,100)
print(max_min(numberTuple))

tuplesList = [('Hema','gmail'),('Raja','phone'),('Riya','Text')]

for name,mode in tuplesList:
     print(name, " : " , mode)

#Files
testFile = open('Test.txt')
print(testFile.tell())
print(testFile.read())
print(testFile.tell())
testFile.seek(0)
print(testFile.tell())
print(testFile.read(8))
if (not testFile.closed):
    print('File closed')
    testFile.close()

with open('Test.txt') as fileHandle:
    for line in fileHandle:
        print(line.rstrip()) #rstrip removes the carriage return
print(fileHandle.closed)

#file modes
"""
open(filename, mode) 
r - read
a - append to an existing file
x - create a new file and write to it
w - clear the contents of the existing file and write to it

to both read and write; use +
file types : t - text file, b - binary file
"""

with open('Test.txt', 'rt') as fileHandle:
    for line in fileHandle:
        print(line.rstrip()) #rstrip removes the carriage return
print(fileHandle.mode) # mode of the current file
print(fileHandle.closed)

#write() to write content to a file
with open('newText.txt','wt') as writeFile:
    writeFile.write("It's almost Halloween...")

with open('newText.txt','r') as readFile:
     print(readFile.read())