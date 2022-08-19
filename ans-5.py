"""Write a python script which takes a three digit number from the user and displays
only its first digit."""

n=int(input("enter a number : "))
while n>=10:
    n=n/10
print("first digit is : ",int(n))   
