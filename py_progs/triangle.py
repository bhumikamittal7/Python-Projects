# cook your code here
T = int(input())
for tc in range(T):
    (a, b, c) = map(int, input().split(' '))
    if (a+b+c==180):
        if (a+b>=c) or (a+c>=b) or (c+b>=a):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
	