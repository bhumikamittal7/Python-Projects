# cook your code here
T = int(input())
def func(a):
    if (a == 'B' or a == 'b'):
        return "BattleShip"
    elif (a == 'C' or a == 'c'):
        return "Cruiser"
    elif (a == 'D' or a == 'd'):
        return "Destroyer"
    elif (a == 'F' or a == 'f' ):
        return "Frigate"
    else:
        return 0
s = []       
for i in range(T):
    a = input()
    s.append(func(a))

for word in s:
    print(word)
