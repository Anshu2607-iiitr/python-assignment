# Q.9
# Program to find determinant of a matrix

A = [[1, 2],
     [3, 4]]

r = len(A)
c = len(A[0])

if r != c:
    print("Not a square matrix")
elif r == 2:
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    print("Determinant =", det)
elif r == 3:
    det = (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
          -A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
          +A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))
    print("Determinant =", det)
else:
    print("Only 2x2 or 3x3 matrix supported")
