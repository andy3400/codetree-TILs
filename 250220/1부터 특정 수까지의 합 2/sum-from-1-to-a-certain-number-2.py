N = int(input())

# Write your code here!

def adder(N):
    if N == 1:
        return 1
    
    return adder( N - 1 ) + N


result = adder(N)
print(result)















