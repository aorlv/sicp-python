#include <stdio.h>

void printSortedArr(int arr[], size_t len);
void insertSort(int arr[], size_t len);
void choiceSort(int arr[], size_t len);
void bubbleSort(int arr[], size_t len);

int main() {
    int arr[] = {5, 3, 7, 1, 2, 6, 4};
    size_t len = sizeof(arr) / sizeof(arr[0]);

    insertSort(arr, len);
    choiceSort(arr, len);
    bubbleSort(arr, len);
}

void printSortedArr(int arr[], size_t len) {
    for(int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void insertSort(int arr[], size_t len) {
    for(int i = 1; i < len; i++) {
        while((i > 0) && (arr[i] < arr[i - 1])) {
            int tmp = arr[i];
            arr[i] = arr[i - 1];
            arr[i - 1] = tmp;
            i--;
        }
    }
    printSortedArr(arr, len);
}

void choiceSort(int arr[], size_t len) {
    for(int i = 0; i < len; i++) {
        for(int j = i + 1; j < len; j++) {
            if (arr[j] < arr[i]) {
                int tmp = arr[j];
                arr[j] = arr[i];
                arr[i] = tmp;
            }
            
        }
    }
    printSortedArr(arr, len);
}

void bubbleSort(int arr[], size_t len) {
    for(int i = 0; i < len; i++) {
        for(int j = i + 1; j < len - i; j++) {
            if (arr[j] < arr[i]) {
                int tmp = arr[j];
                arr[j] = arr[i];
                arr[i] = tmp;
            }
        }
    }
    printSortedArr(arr, len);
}