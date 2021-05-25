# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
#Enter 7, 2, bob, 10, and 4 and match the output below


largest=None
smallest=None
while True:
    i=input("Enter Number:")
    if(i=="done"):
        break
    else:
        try:
            i=int(i)
            if largest is None:
                largest=i
            elif(i>largest):
                largest=i
            if smallest is None:
                smallest=i
            elif(i<smallest):
                smallest=i
        except:
            print("Invalid input")
print("Maximum is",largest)
print("Minimum is",smallest) 
