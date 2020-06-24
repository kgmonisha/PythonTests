#[1,3,2,2].4

def pairsum(l1):
    sum1 = l1[1]
    dict1 = {}
    res = []
    for i in l1[0]:
        diff = sum1 - i
        if diff in dict1:
            res.append([diff,i])
        else:
            dict1[i] = diff
    return res



print(pairsum([[1,3,2,2],4]))