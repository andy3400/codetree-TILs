N = int(input())

for i in range(1, N+1):
    
    if i%3==0:
        print("0", end=" ")

    elif i >=30 and (i//10)%3==0:
        print("0", end=" ")

    else:
        print(i,end=" ")
