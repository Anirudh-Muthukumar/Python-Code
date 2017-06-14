import string
def count(n=5):
    ct=0
    inFile=open('C:\Users\dell\Enthought Canopy environment\loadWords\words.txt','r')
    try:
        line=inFile.readline()
        fields=line.split()
        for i in fields:
            if len(i)==n:
                ct+=1
        print ct            
    except:
        print 'File not opened'

count(int(raw_input('Enter length of word to be searched : ')))
