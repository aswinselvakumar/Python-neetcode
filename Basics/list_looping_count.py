def count_x(nums:list[int],x:int)->int:
    count = 0
    for i in range(len(nums)):
        count+=1
    return count

print(count_x([1,2,3,4],4))