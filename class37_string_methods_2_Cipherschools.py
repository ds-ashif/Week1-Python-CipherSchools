# replace method
# find method
string= "she is beautiful and she is a good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))
print(string.replace("is","was",2))
print(string.replace("is","was",3))

print(string.find("is"))

is_pos1=string.find("is")  #  it will be a number
is_pos2=string.find("is", is_pos1+1)

print(is_pos2)
