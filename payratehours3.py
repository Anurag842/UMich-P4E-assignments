try:
    hrs = raw_input("Enter Hours:")
    hours=float(hrs)
    rte = raw_input("Enter Rate:")
    rate=float(rte)
    if hours<=40:
        pay=rate*hours
    if hours>40:
        pay=rate*40+(rate*1.5*(hours-40))
    
    print pay
except:
    print "Error,input a goddamn number"