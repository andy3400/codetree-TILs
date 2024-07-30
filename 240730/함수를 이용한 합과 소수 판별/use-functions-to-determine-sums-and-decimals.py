def prime(i):
    if i < 2:
        return False

    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            return False
    return True


def cal(a, b):
    count = 0
    for i in range(a, b + 1):
        if prime(i):
            # 각 자리수의 합이 짝수인지 확인
            sum_of_digit = sum(map(int, str(i)))
            if sum_of_digit % 2 == 0:
                count += 1
    return count


def main():
    a, b = map(int, input().split())
    print(cal(a, b))


if __name__ == "__main__":
    main()