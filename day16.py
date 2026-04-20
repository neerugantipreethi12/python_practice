#LISTS PRATICE
nums = [10,20,30,40]
nums.append(50)
nums.remove(20)
print(nums)
#FIND THE LARGEST NUMBER
nums =[5,2,9,1]
print(max(nums))
#REVERSE LIST
nump =[1,2,3,4]
nump.reverse()
print(nump)
#LIST COMPREHENSION
numm = [1,2,3,4]
sqrs =[x*x for x in nums]
print(sqrs)
#TUPLES PRATICE
t =(10,20,30)
print(t[1])
#EXAMPLE CONVERT TUPLE TO LIST
t =(1,2,3)
l = list(t)
l.append(4)
print(4)
#COUNT ELEMENTS
t = (1,2,2,3)
print(t.count(2))
#SETS PRATICE(REMOVE duplicates)
numr =[1,2,2,3,4,4]
unique = set(numr)
print(unique)
#UNION & INTERSECTION 
a = {1,2,3}
b ={3,4,5}
print(a|b)
print(a&b)
#ADD & REMOVE
s={1,2,4}
s.add(3)
s.remove(4)
print(s)


