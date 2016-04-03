def computepay(r,h):
    if h<=40:
        p=r*h
    else:
        p=r*40+(r*1.5*(h-40))
    return p

hrs = raw_input("Enter Hours:")
hours=float(hrs)
rte = raw_input("Enter Rate:")
rate=float(rte)

pay=computepay(rate,hours)
print pay