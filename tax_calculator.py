# Creating a Tax Calculator 


print("""
monthly income tax (%)
0-20000        10%
20k-50k        15%
50k-80k        20%
80k-130k       30%
130k-200k      40%
200k<          50%
""")

while True:
    tax_ratio = input("If you want to check your salary tax type \'Yes\' or \'No\' to exit: ")
    if tax_ratio.lower() == 'yes':
        

        salary = eval(input("Enter your monthly salary: "))
        print("Monthly Salary : ", salary)
        anuual_salary = salary * 12
        print("Annual Salary : ", anuual_salary)

#                   Salary 0 to 20,000

        if salary >= 0 and salary <= 20000:
            tax = (10 / 100) * salary
            print("Monthly Tax: ", tax)
            anuual_tax = tax * 12
            print("Annualy Tax: ", anuual_tax)
    
#                  Salary 20,000 to 50,000

        elif salary > 20000 and salary <= 50000:
            tax = (15 / 100) * salary
            print("Monthly Tax: ", tax)
            anuual_tax = tax * 12
            print("Annualy Tax: ", anuual_tax)

#                  Salary 50,000 to 80,000

        elif salary > 50000 and salary <= 80000:
            tax = (20 / 100) * salary
            print("Monthly Tax: ", tax)
            anuual_tax = tax * 12
            print("Annualy Tax: ", anuual_tax)

#                  Salary 80,000 to 130,000

        elif salary > 80000 and salary <= 130000:
            tax = (30 / 100) * salary
            print("Monthly Tax: ", tax)
            anuual_tax = tax * 12
            print("Annualy Tax: ", anuual_tax)

#                  Salary 130,000 to 200,000

        elif salary > 130000 and salary <= 200000:
            tax = (40 / 100) * salary
            print("Monthly Tax: ", tax)
            anuual_tax = tax * 12
            print("Annualy Tax: ", anuual_tax)

#                  Salary 200,000 >

        elif salary > 200000:
            tax = (50 / 100) * salary
            print("Monthly Tax: ", tax)
            anuual_tax = tax * 12
            print("Annualy Tax: ", anuual_tax)
    
    elif tax_ratio.lower() == 'no':
        print("Good Bye")
        break

    else:
        print("Enter an valid command...")