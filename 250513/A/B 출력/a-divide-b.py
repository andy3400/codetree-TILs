A, B = map(int, input().split())

result = str(A//B)+"."
A %= B

for _ in range(20):
    A*=10
    result += str(A//B)
    A %= B
 
print(result)
