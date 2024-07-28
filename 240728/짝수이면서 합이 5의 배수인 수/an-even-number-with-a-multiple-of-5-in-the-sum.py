def cal(n):
    a = n // 10
    b = n % 10
    if ((a + b) % 5) == 0 and n%2 == 0:
        return "Yes"
    return "No"

def main():
    n = int(input())
    print(cal(n))

if __name__ == "__main__":
    main()