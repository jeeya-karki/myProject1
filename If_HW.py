sal=float(input("Enter your net salary:"))

if(sal<100000):
    print("No tax will be paid.")

elif(sal<3,00,000 and sal>=100000):
    sal=((sal-100000)*0.10)
    print("10% tax will be paid.\n",sal)

elif(sal<7,00,000 and sal>3,00,000):
    sal = ((200000) * 0.10)+((salary-400000) * 0.20)
    print("20% tax will be paid.\n",sal)

elif(sal<15,00,000 and sal>7,00,000):
    sal = ((300000) * 0.10)+((salary - 800000) * 0.30)
    print("30% tax will be paid.\n")

elif(sal<25,00,000 and sal>15,00,000):
    sal = ((300000) * 0.10)+((salary - 800000) * 0.30)+((salary - 1000000) * 0.40)
    print("40% tax will be paid.\n")

elif(sal>25,00,000):
    sal = ((300000) * 0.10) + ((salary - 800000) * 0.30) + ((salary - 1000000) * 0.40)+ ((salary - 1500000) * 0.50)
    print("50% tax will be paid.\n")

else:
    print("Invalid input.")



