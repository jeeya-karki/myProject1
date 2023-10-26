list = [340,"abc",92.56,-79,"Hello Everyone",8036,50.23 ]
print(list[2])
print(list[-2])
print(list[4])

#Slices
print(list[:4])
print(list[:])
print(list[3:])
print(list[5:])

#overwriting
list[-2]=-708.94
print(list)
list[6]=input("Enter a list element:")
print(list)

#append of list
list.append(6055)
print(list[:])

#change the (of a specific index)element of list
list.__setitem__(4,"hello world")
print(list)

#set a value of list in a specfic index or position
list.insert(0,"XYZ")
print(list)

#to remove the element of list
list.remove(-79)
print(list)
