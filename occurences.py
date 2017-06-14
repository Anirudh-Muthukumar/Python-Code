order=raw_input("Enter your order : ")
salad=0
water=0
hamburger=0

for l in order:
    if l=='s':
        salad+=1
    elif l=='w':
        water+=1
    elif l=='h' :
        hamburger+=1
print 'salad:' + str(salad)+' hamburger:'+str(hamburger)+' water:'+str(water)