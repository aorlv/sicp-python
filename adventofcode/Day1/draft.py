"""
import os
print(os.getcwd())

pos = 50
password = 0

with open("/Users/.../input.txt") as f:
    for x in f:
        if x[0] == 'R':
            for i in range(int(x[1:])):
                pos += 1

                if pos > 99:
                    pos = 0
        else:
            for i in range(int(x[1:])):
                pos -= 1

                if pos < 0:
                    pos = 99

        if pos == 0:
            password += 1

print(password)
"""

pos = 50
password = 0

with open("/Users/avo/Study/python/adventofcode/Day1/input.txt") as f:
    for x in f:
        value = int(x[1:])
        steps = 0

        if value > 100:
            password += (pos + value) // 100
            steps = value % 100

        pos = (pos + steps) % 100 if x[0] == 'R' else (pos - steps) % 100

print(250 // 100)
print(password)