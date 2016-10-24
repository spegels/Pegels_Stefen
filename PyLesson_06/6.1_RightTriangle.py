word = input("Please enter word: ")

def RightTri():
    for i in range(len(word), 0, -1):
        print(word[i:len(word)])

RightTri()
