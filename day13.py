# REVERSE A STRING
s ="hello"
print(s[::-1])
# count vowels in a string
s = "education"
count = 0
for ch in s:
    if ch in "aeiou":
        count+=1
    print(count)
# CHECK PALINDROME
s = "madam"
if s ==s[::-1]:
 print("palindrome")
else:
 print("Not palindrome")
# COUNT CHARACTERS
s = "banana"
count = 0
for ch in s:
     if ch =='t':
         count+=1
        print(count)
# REMOVE SPACES
s = "hello world"
print(s.replace(" ",""))
# FIND LENGTH WITHOUT
s = "python"
count = 0
for ch in s:
     count +=1
     print(count)
# FIRST NON REPEATING CHARACTER
s = "aabbtcde"
for ch in s:
     if s.count(ch)==1:
         print(ch)
         break
# CHECK ANAGRAM
s1 = "listen" 
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
#  REVERSE THE EACH WORD OF THE STRING
s ="I LOVE PYTHON"
words = s.split()
result = []
for word in words:
    result.append(word[::-  1])
    output = "".join(result)
    print(output)



 