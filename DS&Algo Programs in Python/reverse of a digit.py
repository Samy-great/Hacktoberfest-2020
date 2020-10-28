#WAP to find reverse of its digit
n=int(input("Enter a no. "))
s=0
while(n!=0):
    r=n%10
    s=s*10+r  # loop
    n//=10
print(s)    


