text = input()
pattern = input()

def find_pattern(text, pattern):
    index = text.find(pattern)
    return index

result = find_pattern(text, pattern)
print(result)
