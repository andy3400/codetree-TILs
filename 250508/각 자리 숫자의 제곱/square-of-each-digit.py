N = int(input())

def f(N):
    if N < 10:
        return N ** 2
    return f(N//10) + f(N%10)**2

print(f(N))