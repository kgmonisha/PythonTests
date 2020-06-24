def reverse(str):
    op = ""
    if len(str) <= 1:
        return str
    n = len(str)
    return str[n-1] + reverse(str[:n-1])

print(reverse("monisha"))