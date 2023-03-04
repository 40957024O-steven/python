one = 1
two = 2

def tool(f1,op,s2):

    if op == "+":
        print (f1+s2)
    elif op == "-":
        print (f1-s2)
    elif op == "*":
        print (f1*s2)
    elif op == "/":
        print (f1/s2)
    elif op == "^":
        print (pow(f1,s2))
    else: 
        print ("無效運算元")