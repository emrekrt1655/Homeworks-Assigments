def tlcd(a, b):
    a_list = list()
    b_list = list()
    c_list = list()
    for i in range(1, a+1):
        if a % i == 0 :
            a_list.append(i)
    for j in range(1, b+1):
        if b % j == 0 :
            b_list.append(j)
    for k in a_list :
        if k in b_list:
            c_list.append(k)
    
    return max(c_list)
            