def max_crossing_sum(arr, left, mid, right):
    # Sol taraftaki maksimum toplamı bul
    left_sum = float('-inf')
    sum_temp = 0
    for i in range(mid, left - 1, -1):
        sum_temp += arr[i]
        if sum_temp > left_sum:
            left_sum = sum_temp

    # Sağ taraftaki maksimum toplamı bul
    right_sum = float('-inf')
    sum_temp = 0
    for i in range(mid + 1, right + 1):
        sum_temp += arr[i]
        if sum_temp > right_sum:
            right_sum = sum_temp

    return left_sum + right_sum


def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = max_subarray_sum(arr, left, mid)
    right_max = max_subarray_sum(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)


# Örnek kullanım
arr = [-2, 3, -5, 4, -1, 6, 2, -5, 4]
max_sum = max_subarray_sum(arr, 0, len(arr) - 1)
max_sum
#çıktı:11