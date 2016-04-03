#calculator

print "For addition press 1"
print "For subtraction press 2"
print "For multiplication press 3"
print "For division press 4"
print "If you're all done press 5"

cmd=float(int(raw_input("Enter operation number:")))


#Addition
if cmd==1:
    print "Ok begin addition"
    first=float(int(raw_input("Enter first number:")))
    second=float(int(raw_input("Enter second number:")))
    result=first+second
    print first,"+",second,"=",result,"(sum)"

#Subtraction
elif cmd==2:
    print "Ok begin Subtraction:"
    first=float(int(raw_input("Enter first number:")))
    second=float(int(raw_input("Enter second number:")))
    result=first-second
    print first,"-",second,"=",result,"(difference)"

#Multiplication
elif cmd==3:
    print "Ok begin multiplication"
    first=float(int(raw_input("Enter multiplicand:")))
    second=float(int(raw_input("Enter multiplier:")))
    product=first*second
    print first,"X",second,"=",product,"(product)"

#Division
elif cmd==4:
    print "Ok begin division"
    print "For decimal division press 1"
    print "For normal division press 2"
    command=float(int(raw_input("Enter Division type:")))
    if command==1:
        first=float(int(raw_input("Enter Dividend:")))
        second=float(int(raw_input("Enter Divisor:")))
        result=first/second
        print first,"/",second,"=",result,"(quotient)"
    elif command==2:
        first=int(raw_input("Enter Dividend:"))
        second=int(raw_input("Enter Divisor:"))
        result1=first/second
        result2=first%second
        print first,"/",second,"=",result1,", remainder =",result2

    
    