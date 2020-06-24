def balanceCheck(str1):
    l1 = []
    matches = set([('{','}'),('[',']'),('(',')')])
    for i in str1:
        if i in ['{','[','(']:
            l1.append(i)
        else:
            if len(l1) == 0:
                return False
            if (l1.pop(),i) not in matches:
                return False
        if l1 == []:
            return True

print(balanceCheck("[[}]"))




