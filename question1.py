age = input("enter your age:")
age = int(age)

if age < 13:
    print("the ticket costs 5$")
elif age < 20:
    print("the ticket costs 10$")
elif age < 100:
    print("the ticket costs 15$")
else:
    print("the ticket costs 20$")