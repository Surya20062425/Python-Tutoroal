# we are going to create a function within another function

def func1():# created a function func1
    s = 'I love learning ' # created a variable with a string 
    def func2(): # created another functiion func2
        print(s) # printin the variable s 
        
    func2()
func1()

# we have to understand 
# the value stored in a function 
# Can be accesed by another function

# example 
# we have created variable s in function func1

# Accessed the value s in another function func2
