for i in range(1042000,702648265):
  temp=i
  sum=0
  
  while i>0:
    r = i%10
    sum=sum+(r*r*r)
    i=i/10
  if(sum==temp):
    break
  print(temp)
