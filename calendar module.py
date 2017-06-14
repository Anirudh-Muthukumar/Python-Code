from datetime import datetime
l=list(map(int,raw_input().split()))
print datetime.weekday(date(l[2],l[1],l[0]))