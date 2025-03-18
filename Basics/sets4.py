def count_unique_words(words:list[int])->int:
    count = 0
    n = set(words)
    for w in n:
        count += 1
    return count

print(count_unique_words(["Hello","Hi","how","Are","You"]))
print(count_unique_words(["Hello","Hi","Hello","Hi"]))