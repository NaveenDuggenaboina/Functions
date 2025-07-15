#CircleAreaPeriEx.py
def circlearea():
    r=float(input("Enter Radius for Cal Area of Circle"))
    ac=3.14*r**2
    print("Area of Circle:{}".format(ac))
def circleperi():
    r = float(input("Enter Radius for Cal Peri. of Circle"))
    pc = 2*3.14 * r
    print("Perimeter of Circle:{}".format(pc))
def menu():
    print("=========================")
    print("\t\t1.Circle Area:")
    print("\t\t2.Circle Perimeter:")
    print("\t\t3.Exit")
    print("=========================")

#main program
while(True):
    menu()
    ch=int(input("Enter Ur Choice:"))
    match(ch):
        case 1:
            circlearea()
        case 2:
            circleperi()
        case 3:
            print("Thx for using this program")
            break
        case _:
            print("Ur Selection of Operation Wrong-try again")