n = int(input("Enter the year you are  in."))
#Check if it is leap or not
if n%100==0 and n%400==0:
  print("it's  a leap year.")
#Non century year
elif n%100!=0 and n%4==0:
  print("it's  a leap year.")
else:
  print("it's not a leap year.")

# for i in range (1,j):
#   d=d*j  
#   print(d)
