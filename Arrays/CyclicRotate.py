#Here we nee to rotate the array by 1
# arr = [1,2,3,4,5]

arr = [1,2,3,4,5]
n = len(arr)
temp = arr[n-1]
for i in range(n-1,0,-1):
    arr[i] = arr[i-1]
arr[0] = temp
print(arr)  

# But if you we want to rotate the element by kth position
# for e.g 
# k = 2 and arr = [1,2,3,4,5]
# output - arr = [4,5,1,2,3]
arr1 = [1,2,3,4,5]
k = 2
n = len(arr1)

for i in range(k):
    temp = arr1[n-1]
    for i in range(n-1,0,-1):
        arr1[i] = arr1[i-1]
    arr1[0] = temp

print(arr1)


