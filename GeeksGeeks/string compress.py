s1 = "AAABBBaaaccc"
s2 = s1[0]
count = 1
for i in s1[1:]:
    if i == s2[-1]:
        count += 1
    else:
        s2 += str(count)
        count = 1
        s2 += i
s2 += str(count)
print(s2)
