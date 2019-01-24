string = input()

if len(string) % 2 != 0 or not 0 <= len(string) <= 100:
    print(0)
    exit(0)

for i in string:
    if i not in ['(', ')', '?']:
        print(0)
        exit(1)

opening = [i for i, char in enumerate(string) if char == '(']
closing = [i for i, char in enumerate(string) if char == ')']

for i, op in enumerate(opening):
    for j, cl in enumerate(closing):
        if op < cl and op != -1 and cl != -1:
            string = string[:op] + '_' + string[op + 1:]
            string = string[:cl] + '_' + string[cl + 1:]
            opening[i] = -1
            closing[j] = -1
        if opening[i] == -1: break

string = string.replace('_', '')

var = ['']

for i in range(len(string)):
    res = []
    for v in var:
        if string[i] == '?':
            res.append(v + ')')
            res.append(v + '(')
        if string[i] == ')':
            res.append(v + ')')
        if string[i] == '(':
            res.append(v + '(')

    var = res.copy()

counter = 0

for v in var:
    opening = [i for i, char in enumerate(v) if char == '(']
    closing = [i for i, char in enumerate(v) if char == ')']

    for i, op in enumerate(opening):
        for j, cl in enumerate(closing):
            if op < cl and op != -1 and cl != -1:
                v = v[:op] + '_' + v[op + 1:]
                v = v[:cl] + '_' + v[cl + 1:]
                opening[i] = -1
                closing[j] = -1
            if opening[i] == -1: break

    v = v.replace('_', '')
    if v == '': counter += 1

print(counter)