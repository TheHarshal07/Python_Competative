# Here we gonna find duplicates in array

# 1 - Brute force
# Time complexity = O(n^2)
t = [2,3,4,2,1,1]

for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i] == t[j]:
            print(t[i])
            

            

# 2 - Bettter solution
# We can make use of Hashmap
# Space complexity = O(2n)
e = [2,3,4,2,1,1]
hashmap = {}
s = set()
for i in e:
    if i in hashmap:
        hashmap[i] += 1
        s.add(i)
    else:
        hashmap[i] = 1
        
print(s)





# 3 - Optimal Solution
# Time complexity = O(n)
# Sapce complexity = O(n)

def FindDuplicates(a):
    n = len(a)
    s = []
    for i in range(n):
        index = a[i]%n
        a[index] += n

    for i in range(n):
        if a[i]/n >= 2:
            s.append(i)
    return s

arr = [2,3,4,2,1,1]
h = FindDuplicates(arr)
print(h)


