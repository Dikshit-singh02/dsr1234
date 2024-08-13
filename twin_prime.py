def prime(n):
    f=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            f=1
            break
        return f
num=int(input("enter starting no:-"))
num1=int(input("enter ending no:-"))
print("twin prime number are ")
for i in range(num,num1+1):
       if prime(i)==0 and prime(i+2)==0:
          print(i," ",i+2);