#LOOPS examples
for i in range(1, 11):
    print(i)

#Print Even Numbers 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#Multiplication Table

num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
 Sum of Numbers from 1 to N

n = int(input("Enter number: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i

print("Sum =", sum)
#While Loop Examples
Print Numbers 1 to 5

i = 1

while i <= 5:
    print(i)
    i += 1
 #Reverse Counting

i = 10

while i >= 1:
    print(i)
    i -= 1
#Sum Until User Enters 0

total = 0
num = int(input("Enter number (0 to stop): "))

while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))

print("Total =", total)
# Break Example
 Stop Loop When Number is 5

for i in range(1, 10):
    if i == 5:
        break
    print(i)
#Continue Example
Skip Number 5

for i in range(1, 10):
    if i == 5:
        continue
    print(i)
#Pass Example
 Pass Statement

for i in range(5):
    pass