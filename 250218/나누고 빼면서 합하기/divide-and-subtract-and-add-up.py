n, m = map(int, input().split())
A = list(map(int, input().split()))

sum_list = []
result = 0


while m > 0:
    if m % 2 == 0:
        sum_list.append(m//2)
        m//=2
    else:
        sum_list.appedn(m-1)
        m = (m-1) // 2


for index in sum_list:
    if 0 <= index < len(A):
        result += A[index]

print(result)
