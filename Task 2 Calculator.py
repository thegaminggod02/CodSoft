#defining functions 
def add(x,y):
 return x+y
 
def sub1(x,y):
 return x-y

def sub2(x,y):
  return y-x
 
def multi(x,y):
  return x*y
  
def div(x,y):
    if b==0:
        return "Division by 0 ERROR!!"
    return x/y

# Step - 2: Main Function1
while True:
    print("Menu: \n","1.Addition \n","2.Subtraction \n","3.Multiplication \n","4. Division \n","5.Exit \n")
    c=int(input("enter your choice:"))

    if c==5:
        print("Exiting Program")
        break
    elif c in(1,2,3,4):
        a=float(input("Enter first operand: "))
        b=float(input("Enter Second operand: "))

        if c==1:
            print("Addition is: ",add(a,b))
        elif c==2:
            if (a>b):
                print("Subtraction is: ",sub1(a,b))
            else:
                print("Subtraction is: ",sub2(a,b))

        elif c==3:
            print("Multiplication is: ",multi(a,b))

        elif c==4:
            print("Division is: ",div(a,b))
    else:
        print("INVALID INPUT!!")
  
   
