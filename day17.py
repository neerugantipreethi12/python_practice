# FINAL DAY OF PRATICE
s = "python"
print(s[::-1])
#check palindrome
s = "madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("NOT palindrome")
#SECOND LARGEST ELEMENT
numS =[10,20,5,8]
numS.sort()
print(numS[-2])
#REMOVE DUPLICATES 
nump =[1,2,2,3,4,4]
unique = list(set(numS))
print(unique)  
#FIND MISSING NUMBER(1 TO N)
nump =[1,2,4,5]

n=5
total = n*(n+1)//2
print(total - sum(nump))
#DICTIONARY CHARACTER FREQUENCY
s = "banana"
freq ={}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
    print(freq)
#WORD COUNT
S = "python is easy python is fun" 
words = s.split() 
freq={}
for w in words:
    freq[w]=freq.get(w,0)+1
    print(freq)
#FUNCTION EXAMPLE
def add(a,b):
    return a+b
print(add(2,3))
#SIMPLE CLASS
class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
s= student("Preethi")
s.display()
#star pattern
for i in range(1,6):
    print("*" * i)
#NON REPEATING CHARACTER
s ="aabbcde"

for ch in s:
    if s.count(ch)==1:
        print(ch)
        break