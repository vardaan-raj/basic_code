# YOU HAVE TO WRITE CODE HERE.... 
# GIVE A PROPER NAME TO YOUR PROGRAM...
#Print list in reverse order using a loop
list = []
n = int(input("enter the number in the list\n"))
for i in range (n):
    ele = input("enter the element\n")
    list.append(ele)
print(list)
j = len(list) -1
list1 = []
while j >=0:
    list1.append(list[j])
    j-=1
print(list1)
