def count_char(word:str)->dict[str,int]:
    count = {}
    for char in word:
        if char not in count:
            count[char] = 0

        count[char]+=1
    
    return count

print(count_char("Aswins"))