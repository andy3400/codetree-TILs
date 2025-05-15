N = int(input())

for i in range(N):
    if (i+1)%2==0 or (i+1)%3==0:
        print("1", end = ' ')
    else:
        print("0", end = ' ')