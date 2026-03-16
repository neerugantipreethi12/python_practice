#  ARRAYS PROBLEM
def sum_array(arr):
    total = 0
    for num in arr:
        total = total + num
        return total
numbers =[10,20,30,40]
print(sum_array(numbers))
# EVEN ELEMENTS IN A ARRAY
arr = [1,2,3,4,5,6,7,8]

for num in arr:
    if num % 2 == 0:
        print(num)
# COUNT NUMBER OF OCCURRENCES
def count_occurrence(arr,x):
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count
numbers = [2,3,4,2,5,2,6] 
print(count_occurrence(numbers,2))  
# FIND MAXIMUM ELEMENT
def find_max(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
        return maximum
numbers = [5,8,2,10,3]
print(find_max(numbers))   
# COUNT EVEN NUMBERS
arr = [1,2,3,4,5,6,7,8]
count = 0
for num in arr:
    if num % 2 ==0:
        count += 1
print("Even numbers:",count)         

    
