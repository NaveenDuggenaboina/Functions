#SimpleIntEx1.py
def Simpleint():
    p=float(input("enter principle amount:"))
    t=float(input("enter time:"))
    r=float(input("enter rate of interrest:"))
    # cal si and totamt to pay
    si=(p*t*r)/100
    totamt=p+si
    print("-"*50)
    print("principle of amount:{}".format(p))
    print("time:{}".format(t))
    print("rate of interest:{}".format(r))
    print("simple interest:{}".format(si))
    print("total amount to pay:{}".format(totamt))
    print("-"*50)

#Main Program
Simpleint()  #Function call