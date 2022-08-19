"""Write a python script which takes a three digit number from the user and displays
only its middle digit."""

n=int(input("enter a number : "))
while n>10:
    mid=n%10
    n=n/10
print("middle digit is : ",int(mid))
