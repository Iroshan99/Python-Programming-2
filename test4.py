import numpy as np

arr1 = np.array([1, 2, 3, 4])
print("Original array:", arr1)

a = [True, False, False, True]
b = arr1[a]

print("Filtered array:", b)

#-----------------------------
print('-------------------------------')

arr2 = np.array([3, 2, 0, 1])

print("Original array:", arr2)
print("Sorted array:", np.sort(arr2))

#-----------------------------
print('-------------------------------')

arr3 = np.array([1, 1, 2, 3, 4, 1])
print("Original array:", arr3)

c = np.where(arr3==1)

print("Index of element 1:", c)