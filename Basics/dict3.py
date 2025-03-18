def list_to_dict(word:list[int])->dict[str,int]:
    my_dict = {}
    for i in range(len(word)):
        w = word[i]
        my_dict[w] = i
    return my_dict

print(list_to_dict(["Aswin","Luke"]))