N = int(input())

def get_divisor(N):
    total = 0
    for i in range(1, N):
        if N % i == 0:
            total+=i
    return total

if get_divisor(N) == N:
    print("P")
else:
    print("N")

