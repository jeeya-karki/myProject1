#Question-1
'''no1=int(input("Enter the value of no1:"))
no2=int(input("Enter the value of no2:"))

if no1==no2 :
    print("Both the number is equal")
else :
    print("Both the numbers are not equal")
'''

#Question-2
'''num=int(input("Enter a number:"))
if(num%2==0) :
    print("This number is Even.",num)
else :
    print("This number is Odd.",num)
'''

#Question-3
'''num=int(input("Enter a number:"))
if(num>=0):
    print("Number is Positive.",num)
else:
    print("Number is negative",num)'''


#Question-4
'''y=int(input("Enter a year:")
      '''

#Question-5
'''a=int(input("Enter your age:"))
if a>=18:
      print("Congratulations! you are eligible for casting your vote")
else:
      print("You are not eligible")'''

#Question-6
'''m=int(input("Enter a number:"))
if m>0:
      print("n=1")
else:
      print("n=0")'''


#Question-7
'''h=int(input("Enter your height in centimeter:"))
if h>0:
      if h<=100:
            print("The person height is dwarf")
      elif h<=180:
            print("The person height is normal")
      else:
            print("The person is heighted person")
else:
      print("Invalid input")'''


#Question-8
'''no1=int(input("Enter no1: "))
no2=int(input("Enter no2: "))
no3=int(input("Enter no3: "))
if no1>no2 and no1>no3:
      print("NO1 is greather than NO2 and NO3.")
elif   no2>no1 and no2>no3:
      print("NO1 is greather than NO2 and NO3.")
else:
      print("NO3 is greather than NO1 and NO2.")'''


#Question-9
'''print("The coordinate point XY is lies between 1 to 500.")
c1=int(input("Enter your coordinate number1:"))
c2=int(input("Enter your coordinate number2:"))
if c1<=100 and c2<=100:
      print("This coordinate points lies in First quadrant ")
elif c1 <= 200 and c2 <= 200:
      print("This coordinate points lies in Second quadrant ")
elif c1 <= 300 and c2 <= 300:
      print("This coordinate points lies in Third quadrant ")
elif c1 <= 400 and c2 <= 400:
      print("This coordinate points lies in Forth quadrant ")
else:
      print("This coordinate points lies in Fifth quadrant ")'''


#Question-10
maths=int(input("Enter Maths marks: "))
sci=int(input("Enter Science marks: "))
eng=int(input("Enter English marks: "))
total=maths+eng+sci
if total>=160:
      print("The candidate is eligible for admission.")
else:
      print("The candidate is not eligible for admission.")
