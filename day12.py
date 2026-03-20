# DYNAMIC ARRAY
 arr =[]
 arr .append(10)
 arr .append(20)

# TRANSPOSE
 matrix = [[1,2],[3,4]]
 transpose = list(zip(*matrix))
# BUBBLE SORT
 arr = [5,2,9,1]
 for i in range(len(arr)):
     for j in range(len(arr)-1):
         if arr[j]>arr[j+1]:
             arr[j],arr[j+1] = arr[j+1],arr[j]
             print(arr)
# 3D ARRAY
 arr =[
     [[1,2],[3,4]],
     [[5,6],[7,8]]]
# ZERO FILL OPERATOR
 num = "25"
 print(num.zfill(5))
# COMMAND LINE ARGUMENT
 import sys
 print(sys.argv)
#  EXAMPLE
 arr = [10 ,20,30]
 arr.append(40)
 arr.remove(20)
 print(arr)
# TRANSPOSE
 matrix =[
    # [1,2,3],
    # [4,5,6]    
 ]
 transpose =[]
 for i in range(3):
     row =[]
     for j in range(2):
         row.append(matrix[j][i])
         transpose.append(row)
         print(transpose)
# 3D ARRAY MORE UNDERSTANDING
arr =[
    [
        [1,2] ,
        [3,4]
    ] ,
    [
        [5,6] ,
        [7,8]
    ]
]
print(arr[0][1][1])
# COMMAND LINE ARUGUMENTS
import sys
name = sys.argv[1]
age = sys.argv[2]
print("name:",name)
print("age:" ,age)
