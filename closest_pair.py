import math

#quick select algorithm to find the location of the n-th element without sorting in O(n) time
def findElementLocation(L, startLoc): 
    nloc = startLoc 

    for pos in range(startLoc+1, len(L)):
        if L[pos][1] > L[nloc][1]: 
            nloc = pos 

    return nloc

#find the x co-ordinate of the point
def x(p):
	return p[0]

#find the y co-ordinate of the point
def y(p):
	return p[1]

#find the distance betwwen two points using formula
def distance(p1, p2):
	return math.sqrt((x(p1) - x(p2))**2 + (y(p1) - y(p2))**2)

#brute force method to find the minimum distance by comparing all the possiblities
def algo(P):
	n = len(P)
	minvalue = float('inf')
	for i in range(0,n):
		for j in range(i+1, n):
			if (distance(P[i], P[j]) < minvalue):
				minvalue = distance(P[i], P[j])
	return minvalue

#find the minimum distance in the given strip (sorted according to y coordinates), of size d.
def close(P, d):
	n = len(P) 
	minvalue = d
	for i in range(0,n): #this is similar to brute force
		j = i+1 #choose all the points in the strip once (at most 7 points)
		while (j<n) and (y(P[j]) - y(P[i]) < minvalue): #check their distance between y - coordinate
			minvalue = distance(P[i], P[j]) #if it is less than given d, change the value of minimum distance
			j +=1
	return minvalue

#Divide and conquer algorithm to recursively find the smallest distance
def closest(P, Q): #take the given list P and it's copy Q which is sorted by y-coordinates
	n = len(P)

	#base cases
	if n<4: 
		return algo(P)

	mid = findElementLocation(P, n//2) #using quick select - T(n) = O(nlogn) complexity
	#mid = n//2  #using merge sort - T(n) = O(nlog^2n) complexity

	#find the midpoint and divide the list into two halves - left and right
	midpoint = P[mid] 
	
	Pleft = P[:mid]
	Pright = P[mid:]

	dleft = closest(Pleft, Q) #recurrsively find the min distance in left side
	dright = closest(Pright, Q) #and on right side

	min_d = min(dleft, dright) #take the min out of left and right

	#now this is the conquer step where we also check for the points in which one is on left and other on right
	P1, Q1 = [], []
	arr = Pleft+Pright

	#for the points closer than d from the midpoint line, append them in arr
	for i in range(0,n):
		if (abs(x(arr[i]) - x(midpoint)) < min_d):
			P1.append(arr[i])
		if (abs(x(Q[i]) - x(midpoint)) < min_d):
			Q1.append(Q[i])

	P1.sort(key = lambda P1: P1[1]) #sort arr according to y coordinates

	minA = min(min_d, close(P1,min_d)) #find the min value from left strip
	minB = min(min_d, close(Q1,min_d)) #find the min value from right strip

	minV = min(minA, minB) 

	return minV #return min of the overall points in the plane

def better_algo(P):
	Q = P 
#	P.sort(key = lambda P: P[0])
	Q.sort(key = lambda Q: Q[1])	#sorting according to y coordinate
	return closest(P, Q)


# testing

# P = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10)]
# P = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 49), 
#		(20,31), (31,41), (42,5), (67,1), (3,6), (2,31), (7,41), (4,5), (0,4)]

# print(algo(P))
# print("#======================================")
# print(better_algo(P))

