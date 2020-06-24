print(bin(10).replace("0b",""))


def decToBin(num):
    if num == 0:
        return
    else:
        decToBin(num//2)
        print(num%2,end="")

decToBin(10)