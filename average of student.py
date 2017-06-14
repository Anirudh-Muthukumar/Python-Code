l=list(map(int,raw_input().split()))
noStud=l[0]
sub=l[1]
for i in range(noStud):
    total=set(map,(float,raw_input().split()))
    print ".2%f"%(total/sub)
    