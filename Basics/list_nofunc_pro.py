def get_sum(my_list:list[int])->int:
    total =0
    for i in range(len(my_list)):
        total +=my_list[i]
    return total
            


print(get_sum([1,2,3]))