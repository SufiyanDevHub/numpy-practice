import numpy as np

# #1d
# arr = np.array([1,2,3,4])
# print(arr[2])

# arr = np.array([1,2,3,4])
# print(arr[0:3])

# # 2d

# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(arr[0])

# arr = np.array([
#     [1,2,3],
#     [4,5,6],
#     [6,7,8]
# ])

# print(arr[1][2])
# print(arr[2][1])


# arr = np.array([
#     [1,2,3],
#     [4,5,6],
#     [6,7,8],
#     [6,7,8],
#     [6,7,8]
# ])

# print(arr[0:5])

# 3d

arr = np.array([[
    [1,2,3,4],
    [10,20,30,40],
    [2,4,6,8],

]])

print(arr[0][1][3])

# 4d

arr = np.array([[
    [
    [1,2,3,4],
    [10,20,30,40],
    [2,4,6,8],
    [3,4,6,8]

]]])

print(arr[0][0][3][2])
print(arr.dtype)
