word = input("Enter word: ")
stop = len(word)
start = 0 

def tree(word, start, stop):
    if start <= stop:
        print(word[0:start])
        start = start + 1
        return tree(word, start, stop)

print(tree(word, start, stop))
