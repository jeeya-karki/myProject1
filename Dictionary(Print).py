dic={201:"ABC",202:"XYZ","AAAAA":55206,212:"YYYYY","Third":"_____"}
print(dic);
print("=================================================================")


#insert
dic["Tree"]="Neem Tree","Banyan Tree","Peepal Tree"
dic["One"]=88302
print("After inserting the new elements:\n",dic)
print("=================================================================")


dic.pop(201);
print("After deleting elements from dictionary:\n",dic)
print("=================================================================")


#length of dictionary
print("The length of dictionary is :\n",len(dic))
print("=================================================================")

#Printing all the keys of dictionary
print("All the keys of dictionary are :\n",dic.keys())
print("=================================================================")

#Printing all the values of dictionary
print("All the values of dictionary are :\n",dic.values())
print("=================================================================")

#printing hole dictionary with key and its values
print("All the items of dictionary are :\n",dic.items())
print("=================================================================")

#Printing hole dictionary uing for_each loop
for i in dic.items():
    print(dic.items())





















