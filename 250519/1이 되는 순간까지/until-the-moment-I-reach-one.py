N = int(input())

count  = 0

def f(N):
    global count
    if N == 1:
        return count

    elif  N % 2 == 0:
        count +=1
        return f(N//2)

    elif  N % 2 != 0:
        count+=1
        return f(N//3)
        
    else:
        return count

print(f(N))