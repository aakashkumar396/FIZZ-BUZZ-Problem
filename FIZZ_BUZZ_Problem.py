#FIZZ BUZZ PROBLEM

# taking user input as number
n = int(input("Enter the number "))

#iteration for n number
for i in range(1,n+1):
    
    #checkig for FIZZBUZZ condition that is multiple of 3*5
    if (i%3==0 and i%5==0):
        print("FIZZ BUZZ")
        
    #checking for multiples of 3    
    elif (i%3==0):
        print("FIZZ")
        
    #checking for multiples of 5    
    elif (i%5==0):
        print("BUZZ")
        
    else:
        print(i)
