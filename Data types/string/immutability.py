# we have to  know string is immutable 

s= "surya"
s = "S" + s[1:]  
print(s)

# we have changed the elements  s with S


# deleting the string 

name =" surya"

del name # by this command we are deleting the string 

# updating 

s = "surya"
s1 = "S" + s[1:]    # we are changing the first element                
s2 = s.replace("sur", "SUR")  # we are replacing the following elements 
# primary element is real and second is replacing element   


# lenght
print(len(name))
# we are fetching the lenght of the string  

# it returns the number of elements in the string 


# changing


name = "Surya prakash"
print(s.upper())# we are converting the total  string to uppercase 

# we used upper()
print(s.lower()) # we are converting the total string to lowercase

# we want to use lower() to convert the string to lowercase the string name 

# strip function

name = "surya prakash nayak "

# once observe the string it contains spaces in betweeen
name.strip() # it actually used to remove the spaces oor gaps 

n1= "surya"

n2="prakash"

print(n1+n2)

#  we have added both strings



#  Formatting string

name = "Surya"
age = 20
print(f"Name: {name}, Age: {age}")

# by the use of f string we can concat any data type 

# it considers the values from the variables

demo = "My name is {} and I am {} years old.".format( "surya", 19)
 
print(s)


# string testing 
name = "surya"
print("su" in name)
print("ry" in name)
