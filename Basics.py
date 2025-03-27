'''
    multi-line comment
    This is a basic python file
'''
print('''Hello world
        My name is
        Ashik''')    
#Output: Hello world
#        My name is
#        Ashik


#to view all supported keywords, modules, functions etc
#open python shell or python native repl on vs code
# to view all keywords type help('keywords')  
# to view all modules type help('modules')
# to view all symbols type help('symbols')



#Defining variables and strings
item = 'Banana'  #String
Item = 'Apple'  #String case senstivive
price = 12.5    #Float

print(item, Item, price)    #print multiple variables
#Output: Banana Apple 12.5
print('Hello' + ' ' + item)   #Concatenation
#Output: Hello Banana



#Defining data types
num = 10    #Integer
num = 10.5  #Float
num = 10 + 5j   #Complex
num = True  #Boolean
word = 'Hello'  #String
make_list = [1, 'Ashik', 3]    #List
#printing their data types
print(type(num))    #Output: <class 'bool'>
print(type(word))   #Output: <class 'str'>
print(type(make_list))  #Output: <class 'list'>



#converting data types
integer = 10
name = 'Ashik'
string_number = '10'

print(integer, int(string_number))   #Output: 10 10
print(name, str(integer))    #Output: Ashik 10



#Math operations
addition = 10 + 5
subtraction = 10 - 5
multiplication = 10 * 5
division = 10 / 5
exponentiation = 10 ** 5
modulus = 10 % 5



#Assignment operators
num = 10
num += 5    #num = num + 5
num -= 5    #num = num - 5
num *= 5    #num = num * 5
num /= 5    #num = num / 5
num **= 5   #num = num ** 5
num %= 5    #num = num % 5



#String operations
### to view all string operations type "dir ("")" in python shell
name = 'Ashik'
name.upper()    #Output: ASHIK  //upper is called a method
name.lower()    #Output: ashik
print(name[0])  #Output: A
print(name[1])  #Output: s
print(name[0:3])    #Output: Ash
print(name[0:]) #Output: Ashik
print(name[-1]) #Output: k, negative index starts from the end
print(name[-3:])    #Output: hik

print(3 * 'Ashik') #Output: AshikAshikAshik

with_escape_char = 'doesn\'t'   #String with escape character
without_escape_char = "doesn't"    #String with double quotes
new_line = 'Hello\nNewyork'   #String with new line
ign_new_line = (r'Hello Newyork')  #String with ignore new line, r for raw string

u = ".2.3.4"
v = u.replace('.', '')
print(v)    #Output: 234

newtex = "my name is al amin ashik. that is a bird."
newtex.count('a') #Output: 6
newtex.count('this') #Output: 0
newtex.find('my') #Output: 0
newtex.find('this') #Output: -1



#List operations
make_list = [1, 'ashik', 3, 4, 5]    
make_list2 = [1, 2, 3]  #List
print(make_list[0]) #Output: 1
print(make_list[1:4])   #Output: ['ashik', 3, 4]
print(len(make_list))   #Output: 5
print(make_list + make_list2)   #Output: [1, 'ashik', 3, 4, 5, 1, 2, 3]
make_list.append(6) #Append to list #output [1, 'ashik', 3, 4, 5, 6]
make_list.insert(1, 2)   #Insert to list #output [1, 2, 'ashik', 3, 4, 5, 6]
make_list.remove(2) #Remove from list #output [1, 'ashik', 3, 4, 5, 6]
del make_list #delete the list

#tuples operations
''' tuples are same as list and can be used as list but they are immutable 
which means content of tuple can't be changed 
tuples are faster and safer than list
tuple is defined by () instead of []'''
make_tuple = (1, 'ashik', 3, 4, 5)
#these are not valid
#make_tuple.append(6) or make_tuple{2} = 6



#Comparison operators
greater_than = 10 > 5
less_than = 10 < 5
greater_than_or_equal_to = 10 >= 5
less_than_or_equal_to = 10 <= 5
equal_to = 10 == 5
not_equal_to = 10 != 5



#Logical operators
i = int(input('input first number')) #input function takes as string so convert
j = int(input('input second number'))
if i > 5 and j < 10:
    print('Both conditions are true')
elif i > 5 or j < 10:
    print('At least one condition is true')



#logic statements
age = 28
isHappy = True
if age > 18 and isHappy == True:
    print('You are an adult and happy')
elif age == 18 or isHappy == True:
    print('You are a teenager or happy')
else:
    print('You are a child')
#Output: You are an adult

if 6%2 == 0:
    print('Even number')
else:
    print('Odd number')
#Output: Even number



#for loop
for i in range(3):
    print('Hello', i)
#Output: Hello 0
#        Hello 1
#        Hello 2

name_list = ['Ashik', 'Rahim', 'Karim']
for name in name_list:
    print(name)
#Output: Ashik
#        Rahim
#        Karim



#while loop
i = 0
while i < 3:
    i = i+1
    print('Hello', i)
#Output: Hello 1
#        Hello 2
#        Hello 3

#making infinite loop and closing
while True:
    user_input = input('Enter q to quit: ')
    if user_input == 'q':
        print('Quitting...')
    break       #break the while loop



#creating functions
def show_name(name):
    print('Hello there', name)
    return
show_name('Ashik') #Output: Hello there Ashik

def multiply (x, y):
    result = x*y
    return result
temp = multiply(5, 6)
print(temp)     #Output: 30


#making a blank function, this will allow you to create a function that you will use later
def show_name():
    pass