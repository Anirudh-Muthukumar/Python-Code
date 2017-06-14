def alphabeticalOrder(word,Wordlist=None):
    current=word[0]
    for i in word:
        if i>=current:
            current=i
        else:
            return False
    return True


            
    