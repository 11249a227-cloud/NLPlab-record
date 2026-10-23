
N=int(input("Enter the number:"))

if N<=0:
   print("Please enter a positive integer greater than 0.")
else:
     a,b=0,1
     print("Fibonacci sequence for given number:")
for i in range(N):
     print(a,end="")
     a,b=b,a+b
