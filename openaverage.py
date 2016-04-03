fname = raw_input("Enter file name: ")

fh = open(fname)

count,thesum=0,0


for line in fh:

    if not line.startswith("X-DSPAM-Confidence:") : continue

    atpos=line.find(":")

    count=count+1

    number=line[atpos+1:]

    number=number.strip()

    numberz=float(number)

    thesum=thesum+numberz

average=thesum/count

print "Average spam confidence:-",average