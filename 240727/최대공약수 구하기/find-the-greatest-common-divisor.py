def gcd(a, b):
    # Uclid : divide a, b and b' gcd is same
    if a < b:
        a,b = b, a
    while b > 0:
        a, b = b, a%b 

    print("%d"%a)


def main():
    a , b = map(int, (input().split()))
    gcd(a, b)

if __name__ == "__main__":
    main()