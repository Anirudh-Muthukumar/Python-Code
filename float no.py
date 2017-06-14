import re
num=float(raw_input())
try:
    if type(num)==float:
        print True
    else:
        print False
except:
    print 'False'