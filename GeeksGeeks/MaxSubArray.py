def kadene(array1):
    max_curr = max_global = array1[0]
    for i in range(1,len(array1)):
        max_curr = max(max_curr,array1[i]+max_curr)
        if max_curr > max_global:
            max_global = max_curr
    return max_curr

print(kadene([1,2,3,-2,5]))
