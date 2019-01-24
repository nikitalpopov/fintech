string = input()

if not (2 <= len(string) <= 1000):
    print()
    exit(1)

counter = [0 for _ in range(26)]

for char in string:
    if 0 <= ord(char)-97 < 26:
        counter[ord(char)-97] += 1

result = ''

for index, element in enumerate(counter):
    if element > 1: result += chr(index + 97)

print(result)