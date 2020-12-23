n = int(input("Enter the count of number you want in your list:"))
lst=[]
for i in range(1,n+1):
    num = int(input("Enter:"))
    if type(num) is int:
        lst.append(num)
    
print("List of numbers entered by you:")
print(lst)

max = lst[0]
for a in lst:
    if a>max:
        max=a
    else:
        pass

print("Largest element:",max)