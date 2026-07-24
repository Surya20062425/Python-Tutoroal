age = 10
if age <= 12:

  # primary condition 
    print("Travel for free.")
else: # it executes when primary condion fails
    print("Pay for ticket.")



age = 25

if age <= 12: # primary condition 
    print("Child.")
elif age <= 19:  # elif defines intermediate  conditions 
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# we are performing match case operation
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:# the operation performed on the basis of input that given 
        print("Two or Three")
    case _:
        print("Other number")
