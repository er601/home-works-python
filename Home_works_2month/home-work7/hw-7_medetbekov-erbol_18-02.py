# ДЗУрок7 Дэдлайн 26.05.2022 23 59
# 1. Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и список в котором необходимо искать.
# 2. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.
# 3. Функция в итоге должна распечатать результат.
# 4. Написать функцию buble_sort или selection_sort, принимающую в качестве входящего параметра не отсортированный список.
# 5. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
# 6. Функция в итоге должна возвращать отсортированный список.


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# --------


def bubble_sort(arr_):
    n = len(arr_)

    for num in range(n - 1):
        for j in range(0, n - num - 1):
            if arr_[j] > arr_[j + 1]:
                arr_[j], arr_[j + 1] = arr_[j + 1], arr_[j]


list_ = [5, 2, 8, 1, 3, 6, 9, 0, 4]
bubble_sort(list_)

print(f"Bubble sort: {list_}")
