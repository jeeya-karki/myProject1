class emp:
    ID=0
    Name=""
    Salary=0
    Department=""

empList=[]

for i in range(2):
    e1=emp()
    e1.ID = int(input("Enter your Employee_ID:"))
    e1.Name = input("Enter your Name:")
    e1.Salary = int(input("Enter your salary:"))
    e1.Department = input("Enter your department name:")
    empList.append(e1)

for e1 in empList:
    e1=emp()
    print("OUTPUT")
    print("####################################################################")
    print("Your Employee_ID is:", e1.ID)
    print("Your Name is:", e1.Name)
    print("Your Salary is:", e1.Salary)
    print("Your Department is:", e1.Department)


