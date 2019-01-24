import re
import math

pattern = re.compile('^[0-9]+ [0-9]+$')
section = input()

if pattern.match(section):
    edges = [int(number) for number in section.split(' ')]
    values = [edges[0]]
    if 1 <= edges[0] <= edges[1] <= 100:
        while True:
            answer = []
            for i in range(len(values)):
                ans = values[i] + 3
                answer.append(ans)
            for i in range(len(values)):
                ans = values[i] * 4
                answer.append(ans)
            values = answer.copy()
            for ans in answer:
                if ans == edges[1]:
                    print(int(math.log(len(answer), 2)))
                    exit(0)

            if len(answer) == len(list(filter(None, [1 if ans == 1 or ans > edges[1] else None for ans in answer]))):
                print(-1)
                exit(1)
    else:
        print(-1)
else:
    print(-1)