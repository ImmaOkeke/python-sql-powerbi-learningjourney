# This is my first python program
print("I am learning Python!")
print("I am enjoying it")

#strings
first_name = "Immaculata"
hobby = "coding"
email = "immaculata.okeke@gmail.com"
print(f"my name is {first_name}")
print(f"my hobby is {hobby}")
print(f"my email is:{email}")

#integers
age = 33
quantity = 20
print(f" I am {age} years old")
print(f"you are buying {quantity} items")

#floats
price = 20.98
gpa = 3.86
distance = 10.5
print(f"The price is ${price}")
print(f"My gpa is: {gpa}")
print(f"The distance is {distance }km")

#booleans
is_expensive = False
if is_expensive:    
    print("The wristwatch is expensive")
else:    
    print("The wristwatch is Not expensive") 


#Typecasting
name = "Immaculata"
age = 33
gpa = 3.86
is_smart = True

age = float(age)
print(age)

#input
name = input("what is your name?:")
age = input("how old are you?:")
age = int(age)
age = age + 1
print(f"hello! {name}")
print(f"Happy Birthday!")
print(f"you are {age} years old")

#Exercise
Length = float(input("enter the length:"))
Width = float(input("enter the width:"))
Area = Length * Width
print(f"the area of the rectangle is: {Area} cm**2")