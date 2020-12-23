n = int(input("Enter the count of numbers you want to input from user:"))
lst = []
even=[]
odd=[]
for i in range(1,n+1):
    a = int(input("Enter:"))
    lst.append(a)

print("List of elements entered:")
print(lst)
for element in lst:
    if element%2==0:
        even.append(element)
    else:
        odd.append(element)
print("\n")
print("List of even elements:")
print(even)
print("List of odd elements:")
print(odd)
        