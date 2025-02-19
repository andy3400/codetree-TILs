N = int(input())

def flower(N):
    if N == 0:
        return
    print(N,end=" ")
    flower(N-1)
    print(N,end=" ")

flower(N)