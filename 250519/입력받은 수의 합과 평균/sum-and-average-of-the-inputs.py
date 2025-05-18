N = int(input())
arr = []
sum = 0

for _ in range(N):
    arr.append(int(input()))

for i in arr:
    sum+=i

avg = sum / N

print(f'{sum} {avg:.1f}')