# program to count uppercase and lowercase characters

string = input("Enter a sentence:")
upper = 0
lower = 0
# iterates through all characters in a string
for i in string:
    if i>='A' and i<='Z':
        upper=upper+1
    elif i>='a' and i<='z':
        lower=lower+1
    else:
        pass

print("No. of uppercase characters:",upper)
print("No. of lowercase characters:",lower)

