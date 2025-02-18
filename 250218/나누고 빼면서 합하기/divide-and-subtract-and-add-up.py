n, m = map(int, input().split())
A = list(map(int, input().split()))

sum_list = []
result = 0  # 초기 result는 0으로 설정

# m이 0보다 클 때까지 반복
while m > 0:
    if m % 2 == 0:  # m이 짝수일 때
        sum_list.append(m // 2)
        m //= 2
    else:  # m이 홀수일 때
        sum_list.append(m - 1)
        m = (m - 1) // 2

# sum_list에서 계산한 인덱스를 통해 결과를 구함
for index in sum_list:
    if 0 <= index < len(A):  # A 배열의 인덱스 범위 내에서만 접근
        result += A[index]

print(result-1)