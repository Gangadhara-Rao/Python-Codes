from numpy import *

#arr = array([1, 2, 3, 4, 5])
#print(arr)

#arr = linspace(0,15)
#print(arr)

#arr = arange(1,15,2)
#print(arr)

#arr = logspace(1,40,5)
#print(arr)

#arr = ones(5,int)
#print(arr)

#arr1 = array([1,2,3,4,5])
#arr2 = array([6,1,9,3,2])
#arr = arr1 + arr2
#print(arr)

#arr = array([1,2,3,4,5])
#print(max(arr))

#arr1 = array([1,2,3,4,5])
#arr2 = array([6,1,9,3,2])
#print(concatenate{arr1,arr2})

#arr1 = array([2,6,8,1,3])
#arr2 = arr1.view()
#arr1[1] = 7
#print(arr1)
#print(arr2)
#print(id(arr1))
#print(id(arr2))

#arr1 = array([2,6,8,1,3])
#arr2 = arr1.copy()
#arr1[1] = 7
#print(arr1)
#print(arr2)
#print(id(arr1))
#print(id(arr2))

# multi dimensional array (matrix)

#arr1 = array([
#    [1,2,3,6,2,9],
#    [4,5,6,7,5,3]
#])
#arr2 = arr1.flatten()
#arr3 = arr2.reshape(2,2,3)
#print(arr3)

m1 = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 2 6 7')
m3 = m1 * m2
print(m3)