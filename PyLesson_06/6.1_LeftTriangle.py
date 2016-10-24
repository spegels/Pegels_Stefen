word = input("Enter word: ")

def LeftTri():
    for i in range(0, len(word), 1):
        print(word[i:len(word)])

LeftTri()
