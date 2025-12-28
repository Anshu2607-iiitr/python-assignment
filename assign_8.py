# Q.8
# Program to calculate MAE and MSE

actual = []
predicted = []

n = int(input("Enter number of values: "))

for i in range(n):
    actual.append(int(input("Enter actual value: ")))
    predicted.append(int(input("Enter predicted value: ")))

if len(actual) != len(predicted):
    print("Lists must be of equal length")
else:
    mae = 0
    mse = 0

    for i in range(n):
        error = actual[i] - predicted[i]
        mae += abs(error)
        mse += error ** 2

    mae = mae / n
    mse = mse / n

    print("MAE =", mae)
    print("MSE =", mse)
