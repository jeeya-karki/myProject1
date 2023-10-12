a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
sum=0
while b!=1:
    a*=2;
    b/=2;
    if(b%2!=0):
            sum=a;
print("sum is:",sum)
