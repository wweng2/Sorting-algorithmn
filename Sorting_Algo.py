import random
import array
import time 
# This is the progation of 10 array with increasing size to be used for the sorting algorithnms
a1 = [0] * 1000
a2 = [0] * 2000
a3 = [0] * 3000
a4 = [0] * 4000
a5 = [0] * 5000
a6 = [0] * 6000
a7 = [0] * 7000
a9 = [0] * 9000
a10 = [0] * 10000
a11 = [0] * 11000


# The Utility function defintions 

def random_array(a,n): # Any function that randomly assign values form 0 to 1000 into an
  # array of n 
                         # size that the user decdes 
  
  for i in range(n):
    
    
	  a[i] = random.randint(0, 1000) # randomly slectes a values and put it in to the array 

  return a
def copyarray(array1,array2): # copy the contents of array 1 to array makinga deepcopy so the # sort
                            # is the done on the same unsort random array for each algoithmn

  for i in range(len(array1)): # Copy the values in each array1 copy to the array 2
    array2[i] = array1[i]

def display_array(array): # utility function to print oput the array to make sure correct
  # values
  for i in range(len(array)):
    print(array[i], end = " ")
  print("/n")

def sqared_time(n): # GEt the time for n^2 so i can use it to graph for asyomptic line to 
  # compare with 
  x = 0
  start_time = time.time() # Caluculate te time and ends hen thenested for loop ends

  for i in range (n):
    for j in range(1,n):
      x += 1
  end_time = time.time()
  taken_time = end_time - start_time # Just the start and end time diffference to say how 
      # long it took and display that 
  print("Here is the time {:0.10f}.\n".format(taken_time) )
 


def sorting_runner(array,n):
  a12 = [0] * n # This is the array that each array will be copy to so that it will be a deep 
   #copy 
  print("Original unsorted array ")
  #display_array(array)

  # only display once since dislpaying it mulplte times in the array will make to mess to be 
  # able to read the time 
  # Insertion sort and producing the time it takes for it 
  copyarray(array,a12)

  print("Starting the  insertionsort of the array")
  
  start_time = time.time()
  insertionsort(a12)
  end_time = time.time()
  
  taken_time = end_time - start_time
  print("Here is the time {:0.10f}.\n".format(taken_time) )

  # This is the selection sort and the time it takes 
  copyarray(array,a12)

  print("Starting the selectionsort of the array")
  
  start_time = time.time()
  selectionsort(a12)
  end_time = time.time()
  
  
  taken_time = end_time - start_time
  print("Here is the time {:0.10f}.\n".format(taken_time) )

  # This is the merge sort and the time it takes 
  copyarray(array,a12)

  print("Starting the mergesort of the array")
  
  start_time = time.time()
  mergesort(a12)
  end_time = time.time()
  
  
  taken_time = end_time - start_time
  print("Here is the time {:0.10f}.\n".format(taken_time) )

  # This is the quicksort and the time it takes 
  copyarray(array,a12)

  print("Starting the quicksort of the array")
  
  start_time = time.time()
  quicksort(a12,0,n-1)
  end_time = time.time()
  
  taken_time = end_time - start_time
  print("Here is the time {:0.10f}.\n".format(taken_time) )
  

# The algorithmns to be used for sorting 
  
def insertionsort(array):

  for i in range(1,len(array)): # This goes from 1 to the n-1, since for insertion sort you 
   #need to 
                                # have to two valeus so it can't start at 0 it needs to have 
   #it be 1 so                                    it can be comapring it with 0

    value = array[i] # The vlaues of i
    j = i - 1 # This is the vlaue that is before i so it will always comapre the two values
    while j >= 0 and value < array[j]: # keep swapping the vlaue unitl j becomes 0 or when 
    #the what value                                        # is not less then whatever vlaue 
    #is in array[j]

        temp = array[j] # Get the value and swap the value
        array[j] = value
        array[j + 1] = temp # The j plus  is i so switch i and j and keep doing this swappign 
   # until it                                # reaches the start of the array
        j -= 1 # Make j goes down so the values comaprethe vlues until it reach the begining
   


def selectionsort(array):
  for i in range(len(array)):

    min_value = i # make the i the min value 

    for j in range(i + 1, len(array)): # i + 1 since the i and i -1 down is already sorted 
  # and is the 
                                        # smallest valeua already , then loop through the 
  # entire array
      if array[min_value] > array[j]:    # if the min value is bigger then what is in 
 # array[j], then 
                                          # make that index the min value
        min_value = j

    temp = array[i]  # Swap the values in each index then keep doing thsi until you reach the 
 # end of array
    array[i] = array[min_value]
    array[min_value] = temp


def mergesort(array):
  if len(array) > 1: # make sure the arry is 1 or higher since 1 length index is already 
 # sorted
    
    half = len(array) // 2 # find the half way point

    left = array[:half] # using string slicing to get the left side of halfway mark  of the  
 # array
    right = array[half:] # uding dtring slicing to get the right side of the halfway mark of 
 # the array
    mergesort(left) # Recursive call left side 
    mergesort(right) # Recursive call the right side 
    merge(array,left,right) # merge the sort left and right side into the array
    

def merge(array,left,right):
    i = 0 # index of the original array
    l = 0  # index of the left array
    r = 0  # index of the right array

    while l < len(left) and r < len(right): # until one side, left or right array run out 
      #keep running

      if left[l] < right[r]: # if the left hand value is smaller then the right hand side, #make 
                            # left i the value in array[i]
        array[i] = left[l]
        l += 1    # Increase the l one to indicate that this vlaue in the elft hand array has# been used 
      
      else : # if the right hand vlaue is smaller, make the right[r] value in the array[i]
        array[i] = right[r]   
        r += 1 # increase the r to idnicate that this value has been used

      i += 1  # increase the orgianl array so it's the unsort index spot

    while(l < len(left)): # To put the rest of the values in the left in to the array , when #the right 
                                # hand arrray is all used 
        array[i] = left[l]
        l += 1
        i += 1

    while(r < len(right)): # put the rest of value of right in if , the left hand array has #all been used
        array[i] = right[r]
        r += 1
        i += 1

def partition(array, l, r): # partition the array and return the value of partition
 
    value = array[l] # The value of pivot to be compared
    left = l - 1 # The left side of the pivot
    right = r + 1 # The right side of the pivot
 
    while (True):# Keep running until you find a value
 
        left += 1 # Increase the value and keep going unitl you find a value that is bigger #than value
        while (array[left] < value):
            left += 1
 

        right -= 1
        while (array[right] > value): # Keep going down until you find a vlue that is less #than value
            right -= 1
 

        if (left >= right): # If left and right meet and that means no more elemnt return the # right side
            return right
 
        array[left], array[right] = array[right], array[left] # Swap the values 
 
 

 
 
def quicksort(array, left, right):
 
    if (left < right): # Make sure the array is not 0 
 
        pivot = partition(array, left, right) # Find the pivot point so you can split the
      # array in half
 
        # Recursivly do the two array, the left side and right side
        quicksort(array, left, pivot)
        quicksort(array, pivot + 1, right) # use the pivot + 1 since the pivot is already in # place
 


# This is the assignment of 10 different array each with an different n and has n random numbers in it

# The sort of an array of 1000 values by the four algoirthmns
n = 1000
a1 = random_array(a1,n)
print("Starting the sorting of all four algorithm by n = 1000")

sqared_time(n) # Get the n^2 time and the displaying the array sorting time for each array
sorting_runner(a1,n)

# Sorting of 20
n = 2000
a2 = random_array(a2,n)
print("Starting the sorting of all four algorithm by n = 2000")

sqared_time(n)
sorting_runner(a2,n)


n = 3000
a3 = random_array(a3,n)
print("Starting the sorting of all four algorithm by n = 3000")

sqared_time(n)
sorting_runner(a3,n)

n = 4000
a4 = random_array(a4,n)
print("Starting the sorting of all four algorithm by n = 4000")

sqared_time(n)
sorting_runner(a4,n)

n = 5000
a5 = random_array(a5,n)
print("Starting the sorting of all four algorithm by n = 5000")

sqared_time(n)
sorting_runner(a5,n)

n = 6000
a6 = random_array(a6,n)
print("Starting the sorting of all four algorithm by n = 6000")

sqared_time(n)
sorting_runner(a6,n)

n = 7000
a7 = random_array(a7,n)
print("Starting the sorting of all four algorithm by n = 7000")

sqared_time(n)
sorting_runner(a7,n)

n = 9000
a9 = random_array(a9,n)
print("Starting the sorting of all four algorithm by n = 9000")

sqared_time(n)
sorting_runner(a9,n)

n = 10000
a10 = random_array(a10,n)
print("Starting the sorting of all four algorithm by n = 10000")

sqared_time(n)
sorting_runner(a10,n)

n = 11000
a11 = random_array(a11,n)
print("Starting the sorting of all four algorithm by n = 11000")

sqared_time(n)
sorting_runner(a11,n)







