A, B = map(int, input().split())

count = 0

for i in range(A, B+1):
    if i % 2 == 0:
        count+=i

print(count)