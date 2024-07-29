def cal_prime(n):
    for i in range(2, int(n**0.5)+1):
        #  나누어 떨어진다면
        if n%i == 0:
            return 0
    return 1
# prime 은  1과 자기 자신을 가진 수 

def repeat_cal(n,m):
    sum = 0
    for num in range(n, m+1):
        if cal_prime(num) == 1:
            sum += num
    return sum

def main():
    n, m = map(int, input().split())
    print("%d"%repeat_cal(n, m))


if __name__ == "__main__":
    main()