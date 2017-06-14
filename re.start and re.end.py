import re
str=raw_input()
sub=raw_input()
for sub in str:
    m=re.search(sub,str)
    print m.start(),m.end()