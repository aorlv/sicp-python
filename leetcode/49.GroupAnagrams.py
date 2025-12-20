from collections import defaultdict

def groupAnagrams(strs):
    hmap = defaultdict(list)                #создаём hashmap с дефолтным типом list
    for word in strs:
        count = [0] * 26                    #создаём массив с 26 значениями (от a до z)

        for i in word:                      
            count[ord(i) - ord('a')] += 1   #определяем какой индекс массива отметить для будущей проверки
        
        hmap[tuple(count)].append(word)     #слова с одинакомым count appendим в значение с нужным ключом (tuple(count))

    return list(hmap.values())


groupAnagrams(["eat","tea","tan","ate","nat","bat"])
groupAnagrams([""])
groupAnagrams(["a"])