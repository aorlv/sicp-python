def insertSort(arr):                               #Сортировка вставкой
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


def choiceSort(arr):                               #Сортировка выборочная
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:                
                arr[i], arr[j] = arr[j], arr[i]



def bubbleSort(arr):                               #Сортировка пузырьком
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def testSorting(sort_algorithm):
    A = [5, 3, 7, 1, 2, 6, 4]
    sorted_A = [1, 2, 3, 4, 5, 6, 7]

    sort_algorithm(A)

    print("Passed" if A == sorted_A else "Failed")

testSorting(insertSort)
testSorting(choiceSort)
testSorting(bubbleSort)
