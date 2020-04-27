import random

"""単純ソートのスクリプト"""
def simplesrt(data):
    n = 0
    d = data
    d_num = len(d)
    for i in range(d_num-1):
        d_min = min(d[i:d_num])
        d_mindex = d[i:d_num].index(d_min) + i
        d[d_mindex] = d[i]
        d[i] = d_min
        n += 1
    print("単純ソートは{}回演算した".format(n))
    return d

"""バブルソートのスクリプト"""
def idou(d,d_index):
    n = 0
    x = d[d_index]
    for ii in range(d_index):
        n += 1
        if d[d_index-(ii+1)] >= x:
            d[d_index-ii] = d[d_index-(ii+1)]
            d[d_index-(ii+1)] = x
        else:
            break
    return n, d
def bublesrt(data):
    n = 0
    d = data
    d_num = len(d)
    for d_index in range(d_num):
        n1, d = idou(d,d_index)
        n += n1
    print("バブルソートは{}回演算した".format(n))
    return d

"""挿入ソートのスクリプト"""
def insrt(d,d_index):
    n = 0
    sub_d = d.copy()
    for i in range(d_index):
        n += 1
        if sub_d[i] > sub_d[d_index]:
            d[i] = sub_d[d_index]
            for ii in range(i,d_index):
                d[ii+1] = sub_d[ii]
            #print("break!")
            break
        else:
            continue
    return n, d
def insrtsrt(data):
    n = 0
    d = data
    d_num = len(d)
    for d_index in range(1,d_num):
        n1, d = insrt(d,d_index)
        n += n1
    print("挿入ソートは{}回演算した".format(n))
    return d

"""クイックソートのスクリプト"""
def i_index(data,index,ref):
    d = data
    d_num = len(d)
    for i in range(index,d_num):
        if d(i) > ref:
            break
    return i
def k_index(data,index,ref):
    d = data
    for k in range(index,-1,-1):
        if d(k) < ref:
            break
    return k
def exchange(data,i,k):
    buf = data[i]
    data[i] = data[k]
    data[k] = buf
    return data

def quiq(data,i,k):
    n = 0
    d = data
    d_num = k
    ref = d[i]
    while i>k:
        i = i_index(data,i,ref)
        print(i)
        k = k_index(data,k,ref)
        print(k)
        if i<k:
            d = exchange(data,i,k)
    d = exchange(data,0,k)
    d = quiq(data,0,k-1)
    d = quiq(data,i,d_num-1)
    return d

def quiqsrt(data):
    n = 0
    d = data
    d_num = len(d)
    print(d)
    print(quiq(d,0,d_num-1))

    print("挿入ソートは{}回演算した".format(n))
    return


"""テスト実行用のスクリプト"""
lists = [random.randint(0,10) for i in range(10)]
quiqsrt(lists)
"""
s_lists = lists.copy()
b_lists = lists.copy()
i_lists = lists.copy()
print("初めは{}".format(lists))
s_lists = simplesrt(s_lists)
print("並び変えると{}".format(s_lists))
print("初めは{}".format(b_lists))
b_lists = bublesrt(b_lists)
print("並び変えると{}".format(b_lists))
print("初めは{}".format(i_lists))
i_lists = insrtsrt(i_lists)
print("並び変えると{}".format(i_lists))
"""
