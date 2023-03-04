"""
credit_card1 = 123
credit_card2 = int(input("Enter your credit card2: "))

if credit_card1 is credit_card2:
    print("True")
else:
    print("False")
"""

"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""

"""
marks = int(input("Enter your marks: "))

if 80 <= marks <= 100:
    print("Grade A")
elif 70 <= marks <= 89:
    print("Grade B")
elif 60 <= marks <= 69:
    print("Grade C")
elif 50 <= marks <= 59:
    print("Grade D")
else:
    print("Grade F")
"""

"""
#service A , 20% 
#service B , 10%

bill = int(input("Your bill: "))
service = input("Enter your service rating: ")

if service == "A":
    total_bill = bill + bill * 0.2
    print(total_bill)
elif service == "B":
    total_bill = bill + bill * 0.1
    print(total_bill)
else:
    print("Thanks.Your Bill " + str(bill))

"""
"""
salary below 1000, tax fre
salary between 1000 and 5000, tax 5%
salary between 5000 and 10000, tax 10%
salary above 10000, tax 20%
"""

salary = int(input("Your Salary: "))

if salary < 1000:
    print("Tax free. Total Salary: " + str(salary))
elif 1000 <= salary < 5000:
    total_salary = salary - salary * 0.05
    print("5% tax. Total Salary: " + str(total_salary))

elif 5000 <= salary < 10000:
    total_salary = salary - salary * 0.10
    print("10% tax. Total Salary: " + str(total_salary))
elif salary >= 10000:
    total_salary = salary - salary * 0.2
    print("20% tax. Total Salary: " + str(total_salary))
else:
    print("Thanks")
