def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Örnek kullanım
arr = [5, -2, 9, -4, 3, -1, 7, -6, 2]
print("Maximum Subarray Sum:", max_subarray_sum(arr))
