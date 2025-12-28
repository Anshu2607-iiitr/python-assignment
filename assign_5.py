# Q.5
# Program to calculate Mean, Median and Mode (Simple method)

l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

if n == 0:
    print("empty list")
else:
    # Mean
    s = 0
    for i in l:
        s = s + i
    mean = s / n

    # Median
    l.sort()
    if n % 2 == 0:
        median = (l[n//2 - 1] + l[n//2]) / 2
    else:
        median = l[n//2]

    # Mode 
    max_count = 0
    mode = l[0]

    for i in l:
        count = 0
        for j in l:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
            mode = i

    print("Mean =", mean)
    print("Median =", median)
    print("Mode =", mode)
