import os
def myaverage(a, b):
    avg = (a+b)/2
    return avg


def get_max_min(data_list):
     max_num = max(data_list)
     min_num = min(data_list)

     return max_num,min_num
    
def get_txt_list(path):
    org_list = os.listdir(path)
    ret_list =[]
    for x in org_list:
        if x.endswith('txt'):
            ret_list.append(x)
    return ret_list

