name=" ashif"
age = 18
print("hello "+name+" your age is "+ str(age)) # this is ugly syntax
# for short, clean and simple syntax , we use string formatting
 #string formatting came in python 2, python 3, python 3.6
print(" hello {} your age is {}".format(name,age))
# as python 3.6

print(f"hello {name} your age is {age}")

# we can  also add something in formatting 
# for example---

print("hello {} your age is {}".format(name,age+2))
