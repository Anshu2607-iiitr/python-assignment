# Q.2
# This program calculates average of a list without using sum()

a = []
n = int(input("Enter number of elements: "))
s = 0

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

for j in a:
    s = s + j

if n == 0:
    print("List is empty")
else:
    avg = s / n
    print("Average =", avg)
