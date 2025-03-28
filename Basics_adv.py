#advance list
nums = [1, 2, 3, 4, 5]
#       0, 1, 2, 3, 4
print (nums.index(3))   #Output: 2
del nums[2]     #delete the element at index 2, #Output: [1, 2, 4, 5]
nums.insert(2, 10)   #insert 3 at index 2, #Output: [1, 2, 10, 4, 5]
nums.insert(0, [1, 2])   #insert list at index 0, #Output: [[1, 2], 1, 2, 10, 4, 5]

#square all number in a list
nums = [x**2 for x in range(10)]
#Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#square all number in a list and output only even numbers
nums = [x**2 for x in range(10) if x%2 == 0]
#output [0, 4, 16, 36, 64]



#creating class and object
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print('Woof! Woof!')
dog1 = Dog('Tommy')
dog1.bark() #Output: Woof! Woof!
dog2 = Dog('Spike')
dog2.bark() #Output: Woof! Woof!

#another example
class Employee:
    #common class for all employee
    empCount = 0
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)
    def displayEmployee(self):
        print('Name: ', self.name, ', Salary: ', self.salary)
#this is going to create first object of employee class
emp1 = Employee('Ashik', 2000)
emp2 = Employee('Rahim', 5000)
emp1.displayEmployee()  #Output: Name: Ashik , Salary: 2000
emp2.displayEmployee()  #Output: Name: Rahim , Salary: 5000
print('Total Employee %d' % Employee.empCount)   #Output: Total Employee 2 



#creating new list from existing list
nums = [1, 2, 3, 4, 5]
my_list = []
for n in nums:
    my_list.append(n) #Output: [1, 2, 3, 4, 5]
#or simply
my_list = [n for n in nums] #Output: [1, 2, 3, 4, 5]



#Sets operations
#creating a set
my_set = {1, 2, 3, 3, 5, 2, 6}
print(my_set)   #Output: {1, 2, 3, 5, 6} #set will remove duplicate values
print(len(my_set))  #Output: 5
if 1 in my_set:
    print('yes')    #Output: yes

#creating an empty set
my_set = set()
my_set.add(1) #add components
my_set.add(2) #add components
my_set.add(3) #add components
print(my_set)   #Output: {1, 2, 3}

#union, intersection, subset, superset
numbers1 = {1, 2, 3, 4, 5, 6}
numbers2 = {4, 5, 6}
print(numbers1 | numbers2)  #Output: {1, 2, 3, 4, 5, 6} #union
print(numbers1 & numbers2)  #Output: {4, 5, 6} #intersection
if numbers1.issubset(numbers2):
    print('yes')    #Output: no
if numbers1.issuperset(numbers2):
    print('yes')    #Output: yes



#Dictionary operations

