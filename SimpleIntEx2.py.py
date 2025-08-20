#SimpleIntEx2.py
def takevalue():
    p = float(input("enter principle amount:"))
    t = float(input("enter time:"))
    r = float(input("enter rate of interrest:"))
    return p,t,r

def calsimpleint():
    p,t,r=takevalue() #Function with Multiline Assighment
    si=(p*t*r)/100
    totamt=p+si
    return p,t,r,si,totamt

def displayresult():
    p,t,r,si,totamt=calsimpleint()   #Function with Multiline Assighment
    print("-" * 50)
    print("principle of amount:{}".format(p))
    print("time:{}".format(t))
    print("rate of interest:{}".format(r))
    print("simple interest:{}".format(si))
    print("total amount to pay:{}".format(totamt))
    print("-" * 50)


#Main Program
displayresult() #Function call


#NOTE: displayresult()--->calsimpleint()--->takevalue() is called Function Chaining