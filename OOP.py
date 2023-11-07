class emp:
    ID=0
    Name=""
    Salary=0
    Department=""


e1=emp()
e2=emp()

e1.ID=int(input("Enter your Employee_ID:"))
e1.Name=input("Enter your Name:")
e1.Salary=int(input("Enter your salary:"))
e1.Department=input("Enter your department name:")

e2.ID=int(input("Enter your Employee_ID:"))
e2.Name=input("Enter your Name:")
e2.Salary=int(input("Enter your salary:"))
e2.Department=input("Enter your department name:")

print("OUTPUT")
print("####################################################################")
print("Your Employee_ID is:",e1.ID)
print("Your Name is:",e1.Name)
print("Your Salary is:",e1.Salary)
print("Your Department is:",e1.Department)

print("OUTPUT")
print("####################################################################")
print("Your Employee_ID is:",e2.ID)
print("Your Name is:",e2.Name)
print("Your Salary is:",e2.Salary)
print("Your Department is:",e2.Department)



