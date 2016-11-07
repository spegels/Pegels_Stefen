word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
word3 = input("Enter third word: ")

def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        word = " " + word + " "
        return makeCenter(word)

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))
    
