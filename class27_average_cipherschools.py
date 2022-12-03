# a= int(input("enter first number: "))
# b= int(input("enter second number: "))
# c= int(input("enter third number: "))

# if we want to take input in single line only then we can write input as:

a,b,c= input("enter these three numbers: ").split(",")

print(f"the average is {int(a)+int(b)+int(c)}")
print("the average is {}".format(int(a)+int(b)+int(c)))
print("the average is",int(a)+int(b)+int(c))
print("the average is "+ str(int(a)+int(b)+int(c)))