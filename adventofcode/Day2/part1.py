res = 0

with open("/Users/avo/Study/python/adventofcode/Day2/test.txt") as file:
    for x in file:
        ranges = x.split(',')

        for i in range(len(ranges)):
            values = ranges[i].split('-')
            firstID = int(values[0])
            secondID = int(values[1])

            while firstID <= secondID:
                mid = len(str(firstID)) // 2
                l = str(firstID)[:mid]
                r = str(firstID)[mid:]
                
                if l == r:
                    print(firstID)
                    res += firstID
                
                firstID += 1

print(res)