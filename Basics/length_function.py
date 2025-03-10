#len(var_name)

my_str="aswin"
print(len(my_str))

def get_longest_word(word1:str,word2:str)->None:
    if len(word1)>len(word2):
        return word1
    else:
        return word2

print(get_longest_word("green","red"))
print(get_longest_word("yellow","orange"))