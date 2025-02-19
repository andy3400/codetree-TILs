n = int(input())

sum  = n +1
def print_num_ordely(n):
    if n == 0:
        return
    print(sum - n, end=" ")
    print_num_ordely(n - 1)

print_num_ordely(n)
print()
def print_num_re_ordely(n):
    if n == 0:
        return
    print(n,end=" ")
    print_num_re_ordely(n - 1)

print_num_re_ordely(n)

    