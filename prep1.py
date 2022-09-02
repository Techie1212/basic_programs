def prime_range(number):
    for i in range(1,number+1):
        count=0
        for j in range(1,i+1):
           if(i%j==0):
              count=count+1
        if(count==2):
             print(i)
number=int(input("enter any number"))
print(prime_range(number))
print(prime_range(number))

