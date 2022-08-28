#==========================================================================================================
#==========================================================================================================

# The timestamps are in 24H format. So, 1921 represents 7:21 PM
def readInput():
    f = open("./names.txt", 'r', encoding='utf8')      # open text file containing names in order
    g = open("./timestamps.txt", 'r', encoding='utf8') # open text file containing timestamps in order
    names = []
    tStamps = []
    subs = []   

    for line in f:
        names.append(line.strip())                     # read names and append to names array

    for line in g:
        tStamps.append(int(line.strip()))              # read timestamps, convert to int and append

    l = len(names)

    if(l != len(tStamps)):                             # In case you make changes to the .txt files 
        print("Error in .txt files")                   # and end up with inequal rows
        exit(-1)    

    for i in range(l):
        subs.append((names[i], tStamps[i]))            # append (name,tStamp) to submissions array
    
    return subs

# For this section to run, place this .py file in 
# a folder containing the attached "names.txt" and "timestamps.txt" files
#==========================================================================================================
#==========================================================================================================

subs = readInput()                                     # subs contains your submissions. It is an array
# print(subs)                                          # where each element is of type (name, tStamp)

# YOUR CODE GOES HERE
#==================================================
def partitionBetter(L, start, stop):
    pivot = L[start][1]
    wall  = start

    for scout in range(start+1, stop+1):
        if L[scout][1] > pivot:
            wall = wall + 1
            L[wall], L[scout] = L[scout], L[wall]
    #LOOP ENDS HERE

    L[wall], L[start] = L[start], L[wall]
    return wall # returning to us the index/position of the pivot

#==================================================
def quickSort(L, start, stop, n): #n stands for n-th largest element

    # protection against stupidity 
    # helps us stop in edge cases
    if stop <= start:
        return

    p = partitionBetter(L, start, stop) #p is the position of the pivot

    if (p-1 == n-1): 
        return L[p]

    if (p - 1 > n-1):
        return quickSort(L, start, p-1, n)

    return quickSort(L, p+1, stop, n-p+start-1)

#==================================================

def modifiedQuickSort(array):
    quickSort(array, 0, len(array)-1, 20)   #place the largest 20 elements (in seemingly random order) from index 0-19
    return array

#==================================================
# Execution

modifiedQuickSort(subs)
for i in range (0, 20):    #to print 20 students with latest timestamps
    print(subs[i])         #print the i-th element of the subs list

#==========================================================================================================
#==========================================================================================================

# EXTRA CREDIT QUESTION
#==========================================================================================================
print("#======================================================")

def findElementLocation(L, startLoc):
    nloc = startLoc # I am assuming that the n-th value is at location startLoc

    # go through the list
    for pos in range(startLoc+1, len(L)):
        if L[pos][1] > L[nloc][1]: # if I find a larger value
            nloc = pos # update my assumption about the location of the n-th value

    # return the location of the n-th value
    return nloc

#==================================================
# Execution

for i in range(0, 20, 1):
    x = findElementLocation(subs, i) # find the location of the n-th value in subs, starting from position i
    subs[i], subs[x] = subs[x], subs[i] #swap the values at position i (subs[i]) and x (subs[x])

for i in range (0, 20):    #to print 20 students with latest timestamps
    print(subs[i])    

#==================================================
#Explanation for the extra credit algo

'''
The above output is generated using the modified version of selection sort to get the worst case time complexity of O(n). 
Here, findMinElementLocation function from the code discussed in the lecture is modified as findElementLocation to find 
the location (index) on the n-th largest element in the list. 

We begin by assuming that the n-th value is at location startLoc. 
Then, we go through the list and if we find a larger value we update our assumption about the location of the n-th value. 
After going through the entire process, return the updated location of the n-th largest element in the list. 
Now we go from position 0 to 19 and find the location of the i-th element and swap the values at position i (subs[i]) and x (subs[x]). 
In the end, we print these 20 elements.

To calculate time complexity - let the time taken to compare two elements be one unit. 
After going through the entire list of nelements, the total time taken is n units. 
Since we repeat this process 20 times, time complexity is O(20n) which is of form O(kn) and is equivalent to O(n) as k is constant. 
'''
#==========================================================================================================
#==========================================================================================================
