name, char= input("enter commaseperated name and character :").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")  # we use lower for case insensitive counts
