import numpy as np

#copy

arr = np.array([1,2,3,4])
x = arr.copy()
arr[0]=42
print(x)
print(arr)

#view

arr = np.array([1,2,3,4])
x = arr.view()
arr[0]=42
print(x)
print(arr)