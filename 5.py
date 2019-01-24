import re

def intersection(sectionA, sectionB):
    res = False

    if sectionA[0] <= sectionB[0] <= sectionA[1]: res = True
    if sectionA[0] <= sectionB[1] <= sectionA[1]: res = True
    if sectionB[0] <= sectionA[0] <= sectionB[1]: res = True
    if sectionB[0] <= sectionA[1] <= sectionB[1]: res = True

    return res

length = int(input())
num = int(input())

if length <= 0 or num < 0:
    print(0)
    exit(1)
if num == 0:
    print(0)
    exit(0)

sections = []

pattern = re.compile('^[0-9]+ [0-9]+$')

for _ in range(num):
    section = input()
    if pattern.match(section):
        edges = [int(number) for number in section.split(' ')]
        if 0 < edges[0] <= edges[1] <= length:
            sections.append(edges)
    else:
        print(0)
        exit(2)

result = sections.copy()
for index1, section1 in enumerate(sections):
    for index2, section2 in enumerate(sections):
        if index1 < index2:
            if intersection(section1, section2):
                result[index1] = []

result = list(filter(None, result))
print(len(result))