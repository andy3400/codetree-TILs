A, B = map(int, input().split())

count = 0

min = min(A, B)
max = max(A, B)

for i in range(min, max+1):
    if i % 5 == 0:
        count+=i

print(count)