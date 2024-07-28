def gcd(n, m):
    if n < m:
        n, m = m, n
    while m > 0:
        r = n % m
        n = m
        m = r

    return n


def lcm(n, m):
    return (n*m) / gcd(n,m)




def main():
    n, m = map(int, input().split())
    print("%d"%lcm(n,m))



if __name__ == "__main__":
    main()