import numpy as np
import random

numArrayElements = 10 #Change this to increase the number of array elements
upperBound = 100 # Change this to increase the upper bound of array elements

#Lower bound is 0

#This section creates an array and fills it with the amount of random numbers
#specified in the range specified

arr = []

for i in range(numArrayElements):
    arr.append(random.randrange(upperBound))

#Prints the unsorted undeleted array
print(arr)

#Variable for an escape condition
done = False

#This should be the bulk of the cpu time, this takes less than O(n^2) time
#This is a fraction of n^2, it does not go as low as O(n*log(n))


#For the number of array elements, execute Stalin Sort, but instead of deleting
#the element out of place, instead delete a completely random element in the
#array

for i in range(numArrayElements):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr.pop(random.randrange(len(arr)))
            break
        if(j+1 == len(arr)):
            done = True

    if done:
        break

#Print what's left of the array
print(arr)
