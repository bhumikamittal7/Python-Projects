def hamming(q,n):
	q[0] = 1
	# complete the rest of the initialization
	i,x2,x3,x5,j2,j3,j5 = 1,2,3,5,0,0,0
	#INV: q[0..i-1] contains the first i values of the sequence; 1<=i<= n.
	# x2 = 2*q[j2] is the minimum value > q[i-1] with the form 2*x for x in q[0..i-1]
	# x3 = 3*q[j3] is the minimum value > q[i-1] with the form 3*x for x in q[0..i-1]
	# x5 = 5*q[j5] is the minimum value > q[i-1] with the form 5*x for x in q[0..i-1]
	while (i < n):
		q[i] = min(x2,x3,x5)

		if (x2 == q[i]):
			j2+=1
			x2 = 2 * q[j2]
		if (x3 == q[i]):
			j3 += 1
			x3 = 3 * q[j3]
		if (x5 == q[i]):
			j5+=1
			x5 = 5 * q[j5]
		i = i+1
	return q
#assert: q[0..n-1] contains the first n values of the sequence
q =[0]*1000
print(hamming(q,1000))