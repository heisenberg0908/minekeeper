# this program is meant to show the difference between naive search and binary search .
# it also shows that binary search is much faster than the naive search
# in binary search we basically divide the array in 2 paerts and keep on doing it , until we get an answer.

import random
import time

def naive_search(l,target):
    #l=list, target=which we want to search 
    for i in range(len(l)):
        if l[i]==target:
            return i
    return -1

def binary_search(l,target,low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high=len(l)-1
    if low>high:
        return -1
    midpoint=(low+high)//2
    if l[midpoint]==target:
        return midpoint
    elif l[midpoint]>target:
        return binary_search(l,target,low,midpoint-1)
    else:
        return binary_search(l,target,midpoint+1,high)
# now we will be calculating the time taken for each search to find our target
# and for this we will be using time module

# firstly we will create a random list of length 10000, to exactly see the time taken by each one to function in big list
# for binary search one condition is that the list should be sorted
length=10000
sorted_list=set()
while len(sorted_list)<length:
    sorted_list.add(random.randint(-3*length,3*length))
sorted_list=sorted(list(sorted_list))

# time taken by the naive searvh to find our target
start=time.time()
for target in sorted_list:
    naive_search(sorted_list,target)
end=time.time()
print("the taken by naive search to find your target was",end-start,"seconds.")


# time taken by the binary search to find our target
start=time.time()
for target in sorted_list:
    binary_search(sorted_list,target)
end=time.time()
print("the taken by the binary search to find your target was",end-start,"seconds ")


    
    