# Q.3
# This program prints Fibonacci series
n = int(input("Enter the number of elements: "))
a=0
b=1
if n <= 0:
    print("invalid")
else:
    for i in range(n):
        print(a, " ")
        c=a+b
        a=b
        b=c

