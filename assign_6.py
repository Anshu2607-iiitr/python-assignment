# Q.6
# Program to calculate Standard Deviation
n = int(input("Enter number of elements: "))
data=[]

for i in range(n):
    data.append(float(input("Enter value: ")))

mean= sum(data)/n

var = 0
for x in data:
        var += (x - mean) ** 2

var = var / n
sd = var ** 0.5

print("Standard Deviation =", sd)
