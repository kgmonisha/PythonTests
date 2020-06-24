def permute(str):
    op = []
    if len(str) == 1:
        return str
    for i,let in enumerate(str):
        print("let is {}".format(let))
        for perm in permute(str[:i]+str[i+1:]):
            print(perm)
            op.append(let+perm)
    return op

print(permute("abc"))