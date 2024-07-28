def contains_369_or_multiple_of_3(n):
    """
    숫자가 3, 6, 9 중 하나를 포함하거나 3의 배수인지 확인합니다.
    """
    if n % 3 == 0:
        return True
    str_n = str(n)
    if '3' in str_n or '6' in str_n or '9' in str_n:
        return True
    return False

def count_special_numbers(a, b):
    """
    주어진 범위 [a, b]에서 3, 6, 9 중 하나를 포함하거나 3의 배수인 숫자의 개수를 셉니다.
    """
    count = 0
    for num in range(a, b + 1):
        if contains_369_or_multiple_of_3(num):
            count += 1
    return count

def main():
    a, b = map(int, input().split())
    result = count_special_numbers(a, b)
    print(result)

if __name__ == "__main__":
    main()