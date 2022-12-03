#strings
name = 'ashif'
print(name[-1])
# string slicing
print(name[-1::-2])
# take user integer
#5user_name, age = input("enter your name and age :").split(",")
# print(user_name)
# print(age)
# len function
print(len(name))
# lower, upper, title method
print(name.upper())
print(name.lower())
print(name.title())
# find, replace , center method
h_pos = name.find("h")
h_pos_2= name.find("h",h_pos+1)
print(h_pos_2)
print(name.center(9,"^"))
print(name.replace("h","H"))
