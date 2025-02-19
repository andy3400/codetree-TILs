n = int(input())

def print_stars(n, current = 1):
    if current > n:
        return
    print("*"*current)
    print_stars(n, current+1)

print_stars(n)