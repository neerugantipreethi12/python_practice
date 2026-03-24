# # # # BASIC CLASS OBJECT
class Student:
  def __init__(self,name,age): 
    self.name =name
self.age = age
s1 = student("Preethi",22)
print(s1.name)
print(s1.age)
 # METHOD  INSIDE CLASS
class student:
    def __init__(self,name):
      self.name = name 
    def greet (self):
      print("HELLO ,my name is",self.name)
      s1 = student("preethi")
    s1.greet()
# # #   MULTIPLE OBJECTS
class car:
      def __init__self(self,brand):
         self. brand = brand
         c1 = car("BMW")
         c2 = car("Audi")
      print(c1.brand)
      print(c2.brand)  
# # #   CLASS WITH DEFAULT VALUES
class Employee:
    def __init__(self,name,salary=20000):
          self.name = name
          self.salary = salary
          e1 = Employee("Ravi")
          e2 = Employee("Priya", 50000)
          print(e1.salary)
          print(e2.salary)  
# # SIMPLE INHERITANCE
class Animal:
      def speak(self):
           print("Animal makes sound")
class Dog(Animal):
           def bark(self):
                print("Dog barks")
d = Dog()
d.speak()
d.bark()



        