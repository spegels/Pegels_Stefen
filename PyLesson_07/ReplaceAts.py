sentence = input("Enter sentence: ")

def replace(sentence):
    while sentence.count("a") > 0:
        sentence = sentence[0: sentence.index("a")] + sentence[sentence.index("a")+1:len(sentence)]

        
        
