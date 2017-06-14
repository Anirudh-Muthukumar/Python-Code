import pylab
import string

def tempdiffplot(lowtemp,hightemp):
    diff=[]
    for i in range(len(lowtemp)):
        diff.append(hightemp[i]-lowtemp[i])
    pylab.figure(1)
    #pylab.plot(range(1,32),diff)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    


inFile=open('C:\Users\dell\Documents\stemp.txt','r')
line=inFile.readline()
fields=line.split()
low=[]
high=[]
if len(fields) < 3 or fields[0].isdigit():
    low.append(int(fields[2]))
    high.append(int(fields[1]))
print high
print low
tempdiffplot(low,high)   