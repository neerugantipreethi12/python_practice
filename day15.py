# REVERSE STRING
s = "I LOVE PYTHON"
words = s.split()
result =[]
for word in words:
    result.append(word[::-1])
output =" " .join(result)
print(output)
# == VS EQUALS
a = "hello"
b = "hello"
print(a==b)
# # IMMUTABLE 
s = "hello"
s[0] = 'H'
#   BASIC CONSTRUCTOR EXAMPLE
class student:
 def __init_(self):
  print("constructor called")
s1 = student
#  CONSTRUCTOR WITH PARAMETER
class student:
     def __init__(self,name,age):
        self .name = name
        self .age =age
s1 = student("Preethi",22)
print(s1.name,s1.age)
# DEFAULT CONSTRUCTOTR VALUES
class Student:
    def __init__(self,name="Unknown",age =0):
        self.name = name
        self.age =age
s1 = Student()
print(s1.name,s1.age)
# MULTIPLE OJECTS EXAMPLE
class car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
c1 = car("BMW",5000000) 
c2 = car("Audi",4000000)
print(c1.brand)
print(c2.brand) 
    
        
