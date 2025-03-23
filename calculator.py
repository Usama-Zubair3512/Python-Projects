def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    return a/b

print("select Operation: \n"
       "1. Add \n"
       "2. subtract \n"
       "3. multiply \n"
       "4. division \n"
       )

select= int(input())

n1=float(input("Enter first number:" ))
n2=float(input("Enter second number:"))

if(select==1):
    print(n1,"+",n2,"=",add(n1,n2))
elif(select==2):
    print(n1,"-",n2,"=",sub(n1,n2))
elif(select==3):
    print(n1,"*",n2,"=",multiply(n1,n2))
elif(select==4):
    print(n1,"/",n2,"=",div(n1,n2))