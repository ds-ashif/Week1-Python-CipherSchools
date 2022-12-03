number=input("enter the number: ")
total=0
i=1
while i< len(number):
    total += int(number[i])
    i += 1
print(total)