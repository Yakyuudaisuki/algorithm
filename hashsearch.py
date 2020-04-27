
def hash_index(data,hash_num):
    return data%hash_num
def zero_hantei(data):
    return data == 0
def eq_hantei(data,srch_num):
    return data == srch_num

def hash_list(data, hash_num):
    hash_list = [0] * hash_num
    for i in range(len(data)):
        index = hash_index(data[i],hash_num)
        while zero_hantei(hash_list[index]) == False:
            index += 1
            if index >= len(hash_list):
                index = 0
        hash_list[index] = data[i]
    return hash_list

def hash_srch(data, hash_num, srch_num):
    index = hash_index(srch_num, hash_num)
    while (eq_hantei(data[index],srch_num) == False)\
            and (zero_hantei(data[index]) == False):
        index += 1
        if index >= len(hash_list):
            index = 0
    return eq_hantei(data[index],srch_num)

list = [3,5,11,45,32,14,73,67,1,43]
list_num = 2*len(list)
h_list = hash_list(list, list_num)
print(h_list)
h_srch = hash_srch(h_list, len(h_list), 8)
print(h_srch)
