import pylab
interest=float(raw_input('Enter interest rate : '))
years=int(raw_input('Enter no. of years : '))
principal=float(raw_input('Enter principal : '))
values=[]
for i in range(years+1):
    values.append(principal)
    principal+=(principal*interest)
pylab.plot(range(years+1),values,'r')
pylab.title('Compound Interest ',fontsize=25,color='b-')           # 'bo' for points
pylab.xlabel('Years of compunding ',fontsize=20,color='y')
pylab.ylabel('Value of Principal ($) ',fontsize=20,color='y')
pylab.show()
