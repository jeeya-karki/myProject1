std_list=[]
std=["ID","Name","Maths","Sci","S.S"]

for i in range(3):
    student=[]
    for data in std:
        if data=="Name :":
            student.append(input("Enter "+data))
        else:
            student.append((input("Enter "+data)))

            student.append(student[-2]+student[-1])
            std_list.append(student)

print("\n output :\n")
for student in std_list:
    for index in range(len(std_list)):
        print(std[index],student[index])
        print("Total Marks :",student[-1])
        print("***************************************")