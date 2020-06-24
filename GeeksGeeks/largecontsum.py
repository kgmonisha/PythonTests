def largecontsum(arr1):
    current_sum = max_sum = arr1[0]
    start = end = 0
    for i in arr1[1:]:
        current_sum = max(current_sum + i, i)
        max_sum = max(current_sum, max_sum)
        print(max_sum)
    return max_sum

print(largecontsum([1,2,-1,4,5,10,-10]))