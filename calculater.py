def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
a=float(input("Enter the number:"))
b=float(input("Enter the number:"))
operation=input(("choice an opration: \n1)addition\n2)substarction\n3)multipication\n4)division\n"))
if operation=="+":
    c=add(a,b)
    print(f"an addition of {a} and {b} is :",c)
elif operation=="-":
    d=sub(a,b)
    print(f"an addition of {a} and {b} is :",d)
elif operation=="*": 
    e=mul(a,b)
    print(f"an addition of {a} and {b} is :",e)
elif operation=="/":
    f=div(a,b)
    print(f"an addition of {a} and {b} is :",f)
else:
    print("Invalid opration,Please chioce right opration.")

