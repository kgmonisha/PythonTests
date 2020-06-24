import re
with open("abc.txt","r+") as fd:
    lines = fd.readlines()
    for line in lines:
        regex = re.search("good",line)
        if regex:
            print(line)
        fd.write(re.sub("good","check",line))
fd.close()