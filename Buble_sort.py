def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
        if not swapped:
            break  # Eğer iç döngüde hiç değişim olmadıysa, dizi sıralıdır
    return arr

# Örnek kullanım
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
sorted_arr