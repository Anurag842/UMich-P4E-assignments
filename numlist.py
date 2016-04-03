count=0
total=0
while True:
    inp=raw_input("Enter number:")
    
    
    
    
    
    try:
        num=float(inp)
    except:
        print 'enter a number'
        continue
    count=count+1
    total=total+num
    if inp=='done': break
    
print "average=",total/count,"total=",total,"count=",count