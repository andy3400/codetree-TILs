def find_Min(a, b, c):
    result = min(a, b, c)

    return result


def main():
    a, b, c = map(int, input().split())
    print("%d"%find_Min(a, b, c))

if __name__ == "__main__":
    main()