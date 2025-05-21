N = int(input())

def cal(N):
    if N == 0 or N == 1:
        return 1
    return N * cal(N-1)

print(cal(N))
    