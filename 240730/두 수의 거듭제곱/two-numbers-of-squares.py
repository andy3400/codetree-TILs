def cal(a, b):
    result = 0

    result = a**b

    return result

def main():
    a, b = map(int, input().split())
    print("%d"%cal(a, b))

if __name__ == "__main__":
    main()