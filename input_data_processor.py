# question 2 task 1

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if int(len(first_name)) >= 2:
    print("The length of your first name is: ", len(first_name))
else: 
    print("Error, first name should be at least 2 characters.")

if int(len(last_name)) >= 2:
    print("The length of your last name is :", len(last_name))
else:
    print("Error, last name should be at least 2 characters.")