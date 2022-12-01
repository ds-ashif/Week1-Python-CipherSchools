# strings are immutable ----- we cant change the string

string="string"
#string[1]="T"
#print(string[1]) #----- it will give erroe because string is immutable
print(string.replace("t","T"))
#print(new_string)