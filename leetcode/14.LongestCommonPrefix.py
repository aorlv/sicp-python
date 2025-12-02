def longestCommonPrefix(strs):
    result = ""
    
    if len(strs) == 0:
        return result
    elif len(strs) == 1:
        result += strs[0]
        return result
    
    min_range = min(len(i) for i in strs)

    for i in range(min_range):
        c = strs[0][i]

        for j in range(len(strs)):
            if strs[j][i] != c:
                break
        else:
            result += strs[j][i]

    print(result)
    return result

longestCommonPrefix(["flower","flow","flight"])
longestCommonPrefix(["dog","racecar","car"])
longestCommonPrefix(["dog","doggy","dogster"])