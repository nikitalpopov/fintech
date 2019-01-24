import re

size = int(input())
if not 3 <= size <= 100:
    print('NO')
    exit(1)

poly = []
pattern = re.compile('^[+-]?([0-9]*[.])?[0-9]+ [+-]?([0-9]*[.])?[0-9]+$')
for _ in range(size):
    section = input()
    if pattern.match(section):
        edges = [float(number) for number in section.split(' ')]
        poly.append((edges[0], edges[1]))
    else:
        print('NO')
        exit(1)

string = input()
point = []
if pattern.match(string):
    point = [float(number) for number in string.split(' ')]
else:
    print('NO')
    exit(1)

inside = False

p1x, p1y = poly[0]
for i in range(1, size + 1):
    p2x, p2y = poly[i % size]
    if p1y == p2y:
        if point[1] == p1y:
            if min(p1x, p2x) <= point[0] <= max(p1x, p2x):
                inside = True
                break
            elif point[0] < min(p1x, p2x):
                inside = not inside
    else:
        if min(p1y, p2y) <= point[1] <= max(p1y, p2y):
            xinters = (point[1] - p1y) * (p2x - p1x) / float(p2y - p1y) + p1x

            if point[0] == xinters:
                inside = True
                break

            if point[0] < xinters:
                inside = not inside

    p1x, p1y = p2x, p2y

if inside: print('YES')
else: print('NO')