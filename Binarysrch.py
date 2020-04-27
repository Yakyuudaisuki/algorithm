def binarysrch1(data, srchnum):
    sdata = sorted(data)
    half = len(sdata)//2
    found = False
    a = sdata[half]
    if half == 0:
        if a == srchnum:
            found = True
        return found
    else:
        if a > srchnum:
            newdata = sdata[0:half]
        elif a < srchnum:
            newdata = sdata[half:len(sdata)]
        else:
            found = True
            return found

    return binarysrch1(newdata, srchnum)

def binarysrch2(data, srchnum):
    sdata = sorted(data)
    head = len(sdata)
    tail = 0
    found = False
    while head > tail:
        half = (head+tail)//2
        a = sdata[half]
        if a > srchnum:
            head = half
        elif a < srchnum:
            tail = half
        else:
            found = True
            break
    return found

numbers = range(0,100)
flag1 = binarysrch1(numbers,99)
flag2 = binarysrch2(numbers,99)
print("{},{}".format(flag1,flag2))
