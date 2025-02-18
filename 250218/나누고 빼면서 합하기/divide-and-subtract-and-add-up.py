n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

def get_answer():
    global m
    
    return_value = 0
    while m:
        return_value += A[m]

        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return return_value

print(get_answer())