from operator import itemgetter

def topKFrequent(nums, k):
    #До этого додумался сам
    hmap = {}

    for num in nums:
        if num not in hmap:
            hmap[num] = 0
        hmap[num] += 1

    sorted_dict = sorted(hmap.items(), key=itemgetter(1), reverse=True)
    result = [k for k, v in sorted_dict[:k]]
    return result

    """
    bucket sort подсмотрел
    count = {}                                      #создаём dict, чтобы посчитать сколько раз встретится число
    freq = [[] for n in range(len(nums) + 1)]       #создаём массив, чтобы подставить в него значение, где индекс будет равен частоте

    for n in nums:
        count[n] = count.get(n, 0) + 1              #считаем количество значений (аналог того, что на 24й строке)
    for n, c in count.items():
        freq[c].append(n)                           #вставляем значение в массив, где индекс равен частоте появления в nums

    res = []                                        
    for i in range(len(freq) - 1, 0, -1):           #цикл в обратном порядке
        for n in freq[i]:                           #ищем значение n в массиве, идя в обратном порядке
            res.append(n)                           #и добавляем их в финальный массив с результатом
            if len(res) == k:                       #когда массив достигнет k значений - возвращаем результат
                return res
    """

topKFrequent([1,1,1,2,2,3], 2)
topKFrequent([1], 1)
topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)
