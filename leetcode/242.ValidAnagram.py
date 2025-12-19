def isAnagram(s, t):
    if len(s) != len(t):
        print("False")
        return False
    
    hmap_s = createHashmap(s)
    hmap_t = createHashmap(t)

    if hmap_s == hmap_t:
        print("True")
        return True
    print("False")
    return False


def createHashmap(string):
    hmap = {}

    for ch in string:
        if ch in hmap:
            hmap[ch] += 1
        else:
            hmap[ch] = 1
    return hmap

isAnagram("aacc", "ccac")
isAnagram("rat", "car")