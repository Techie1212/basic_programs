while(1):
  string=input("enter a value:")
  if(string=="quit"):
     print("Bye!!")
     break
  number=int(string)
  if(number>0):
       print("number is positive")
  elif(number<0):
       print("number is neagative")
  else:
       print("number is zero")
 ##
def prime(a):
      count=0
      for i in range(1,a+1):
         if(a%i==0):
             count=count+1
      if(count==2):
           return True
      else:
           return False
while(1):
  string=input("enter a value:")
  if(string=="quit"):
      print("bye!!")
      break
  a=int(string) 
  print(prime(a))

