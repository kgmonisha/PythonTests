str1 = "   space here "
str1 = str1.strip(" ")
l1 = str1.split(" ")
print(" ".join([l1[i] for i in range(len(l1)-1,-1,-1)]))


