# --- PERSONAL INFO ---
name = input("What is your name? ")
print("Hello " + name)

food = input("What is your favourite food? ")
print("My favourite food is " + food)

age_input = input("How old are you? ")

name = "Furkan"
height = 183
print(name + " is " + str(height) + " cm tall.")


# --- CALCULATOR ---
print("\n--- Calculator ---")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

result = int(num1) + int(num2)
print("Result: " + str(result))


# --- MATH OPERATORS ---
x = 9
y = 3

print(x ** y)
print(x // y)
print(x % y)


# --- STRING METHODS ---
name = 'Furkan'
print(name.upper())
print(name.lower())
print(len(name))


# --- CONDITIONALS (WEATHER) ---
is_rainy = True
is_hot = False

if is_rainy:
    print("Take your umbrella and eat something.")
if is_hot:
    print("Don't eat heavy food.")


# --- CONDITIONALS (LICENSE CHECK) ---
has_license = True
has_car = False

if has_car and has_license:
    print("You can drive a car!")
elif has_license and not has_car:
    print("You have a license, but you need a car.")
else:
    print("You cannot drive right now.")


# --- AGE CHECK ---
age = 19

if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are too young.")


# --- LOOPS ---
print("\n--- Counting ---")
i = 1
while i <= 10:
    print("Number: " + str(i))
    i = i + 1


# --- LISTS ---
students = ["Rıdvan", "Furkan", "Melih", "Engin", "Vildan"]
print(students[0:3])

print("\n--- Student List ---")
for student in students:
    print("Student Name: " + student)

