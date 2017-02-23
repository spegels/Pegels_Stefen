word = input("Enter word: ")

def revTri():
    for i in range(len(word), 0, -1):
        print(word[0:i])
revTri()
