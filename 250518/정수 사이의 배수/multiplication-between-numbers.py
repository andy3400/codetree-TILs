A, B = map(int, input().split())

sum = 0
count = 0
avg = 0.0

for i in range(A, B+1):
    if i % 5 == 0 or i % 7 == 0:
        sum+=i
        count+=1

avg = sum/count

print(f'{sum} {avg:.1f}')