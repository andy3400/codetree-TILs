N = int(input())

def f(N):
    if N == 1 or N == 2:
        return 1
    else:
        # N이 4라면 f(3) +f (2)이고, f(2) +f(1) +f(2)
        return f(N-1) + f(N-2)
print(f(N))