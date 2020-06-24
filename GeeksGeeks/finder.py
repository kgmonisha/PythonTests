def finder(num1,num2):
    res = 0
    print(num1+num2)
    for num in num1+num2:
        res ^= num
        print(num,res)
    return res

print(finder([1,2,3,4,5],[1,2,3]))