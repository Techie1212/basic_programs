"""
i=1
while i<=4:
  print("# ",end=" ")
  j=1
  while j<=4:
    print("# ",end=" ")
    j+=1
  i+=1
  print()
 
for i in range(1,101):
   if(i%3==0 or i%5==0):
      continue
   print(i)
"""
for i in range(4):
   for j in range(4-i):
      print(i+1,end=" ")
   print()
