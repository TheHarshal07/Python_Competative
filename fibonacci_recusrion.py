#Here we wil gonna write fibonacci series using recursion


def fibonacci(num):
    if (num <= 1):
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n = 5
print("The fibonacci series :")
for i in range(n):
    print(fibonacci(i) ,end=" ")