# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

print('Question 1')
employee_first_name = "Serena"
employee_last_name = "Killion"

# You have decided the format of the email should be: Serena Killion -> serena.killion@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's concatenate the lowercase versions of the employee first and last name in two new variables
lower_first = employee_first_name.lower() 
lower_last = employee_last_name.lower()

# 1.2 TODO: Combine the lowercase first and last name together with a . and save it to a variable joined_names
joined_names = lower_first + '.' + lower_last

# 1.3 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email'
email = joined_names + '@ripplemedia.com'

# 1.4 TODO: Print out the email using a f string with the message: Your new company email is {email}

print(f"Your new company email is {email}")
print()


print('Question 2')
#Recall the temperature challenge from last week where we converted tempeartures from celsius to fahrenehit and vice versa
#The formula from f to c is (f_temp-32)*5/9
#The formula from  c to f is ((c_temp*9/5)+32)

f_temp = 100
c_temp = 5
print()

# 2.4 TODO: Using an f string, convert f_temp to celsius and print out the result formating the two variables inside the string
#Example print statement: 100 degrees f is 37.77777777777778 in celsius 

f_to_c = (f_temp-32)*5/9
print(f"{f_temp} degrees f is {f_to_c} degrees celsius")

#2.5 TODO: Using an f string, convert c_temp to fahrenheit and print out the result
#Example print statement: 5 degrees celsius is 41.0 degrees fahrenheit 

c_to_f = (c_temp*9/5)+32
print(f"{c_temp} degrees celsius is {c_to_f} degrees f")


print()

print('Question 3')

#3.1 TODO: Using the greater than (>) or less than operators (<) write a TRUE statement and set it to a variable t 
t = 5 > 2 #replace 0 with your true statement
print(t) #should print out True


#3.1 TODO: Using the greater than (>) or less than operators (<) write a FALSE statement and set it to a variable f 
f = 5 < 2 #replace 0 with your false statement
print(f) #should print out False

print()

#3.2 TODO: using the t and f variables, print out the words true and fale in ALL CAPS
#Hint! Think about what datatype t and f are and what datatype you need to use the upper function

print(str(t).upper())
print(str(f).upper())

print()


#What do you think will print out if you convert t and f into integers?
#3.3 TODO: Convert true and false booleans into an integer and see what prints out

print(int(t))
print(int(f))