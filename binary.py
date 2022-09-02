number=int(input("enter a number:"))
sum=0
count=0
while(number!=0):
    rem=number%10
    number=number//10
    sum=sum+(2**count)*rem
    count=count+1
print(sum)
