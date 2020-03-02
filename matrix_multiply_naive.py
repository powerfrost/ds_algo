"""
Program to multiply two matrices using nested loops
This is the naive method
"""

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for xr in range(len(X)):
   # iterate through columns of Y
   for yc in range(len(Y[0])):
       # iterate through rows of Y (which is also columns of X)
       for xc_yr in range(len(X[0])):
           result[xr][yc] += X[xr][xc_yr] * Y[xc_yr][yc]
           print(result)

for r in result:
   print(r)
