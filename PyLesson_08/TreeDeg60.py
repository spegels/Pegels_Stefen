word = input("Enter word: ")
stop = len(word)
start = 0 

def tree(word, start, stop):
    if start < stop:
        start += 1
        print(word[0:start])
        return tree(word, start, stop)
    else:
        word = ""
        return word


print(tree(word, start, stop))
