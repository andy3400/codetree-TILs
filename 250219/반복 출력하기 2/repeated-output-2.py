n = int(input())

# Write your code here!
def print_repeate(n):
    if n == 0:
        return
    print_repeate(n-1)
    print("HelloWorld")

print_repeate(n)