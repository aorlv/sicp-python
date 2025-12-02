pos = 50
password = 0

with open("/Users/avo/Study/python/adventofcode/Day1/input.txt") as f:
    for x in f:
        if x[0] == 'R':
            for i in range(int(x[1:])):
                pos += 1

                if pos > 99:
                    pos = 0
                if pos == 0:
                    password += 1
        else:
            for i in range(int(x[1:])):
                pos -= 1

                if pos < 0:
                    pos = 99
                if pos == 0:
                    password += 1

print(password)