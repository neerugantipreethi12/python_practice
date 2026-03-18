# ARRAY BASED EXAMPLES
# SUM OF ELEMENTS IN ARRAY
arr = [10,20 ,30,40,50]
total = 0
for i in arr:
     total = total + i
     print("sum" , total)
# FIND EVEN NUMBERS IN ARRAY
arr = [1,2,3,4,5,6]
for i in arr:
    if i % 2==0:
         print(i)
# COUNT OCCURRENCES OF ELEMENT
    arr =[1,2,2,3,3,2,4]
    count = 0
    num =3
    for i in arr :
     if i == num:
         count += 1
         print("count :", count)
# FIND MAXIMUM ELEMENT
arr = [5,2,9,1,10]
max_val =arr[0]
for i in arr:
     if i >max_val:
         max_val = i
print("max:", max_val)
# REVERSE AN ARRAY
arr =[1,2,3,4]
rev=[]

for i in arr:
     rev = [i]+rev
     print(rev)
# REMOVE DUPLICATIONS
arr = [1,23,43,34,43,23,43]
unique = []
for i in arr:
     if i not in unique:
         unique .append(i)
         print(unique)
# SEARCH AN ELEMENT
arr = [10,20,30]
key = 10
for i in arr:
     if i == key:
         print("found")
        
     else:
      print("NOT FOUND")
# 

