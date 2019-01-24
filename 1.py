def palindrome(s):
    return all(s[i] == s[-(i + 1)] for i in range(len(s) // 2))

x = int(input())
counter = 0

if x <= 100000:
    for i in range(x):
        if palindrome(str(i)): counter += 1

print(counter)