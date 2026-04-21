#spliting
list =[10,9,8,7,6,5,4,3,2,1]
list1=list[:5]
list2=list[5:]
list2.extend(list1)
print(list1)
print(list2)

size = 2
for i in range(0,len(list),size):
    print(list[i:i+size])

#second largest element 
list.reverse()
print(list)
min = list[0]
secondmin= list[1]
for i in range(len(list)):
    if list[i] < min:
        secondmin = min
        min = list[i]
    elif list[i]< secondmin:
        secondmin = list[i]

print(min, secondmin)


