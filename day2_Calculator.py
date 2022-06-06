# Primitive Data Type
# 1. Data Type
#       String
#print("Hai Witaradya"[0])
#print("123" + "456")

#       Integer
#angka = 123456789
#angka2 = 123_456_789

#       FLoat
#3.14

#       Boolean
#   true or false   


# 2. Type Error, Type Checking, and Type Conversion
# type() = to check what kind of type data
# str() = casting data from any type data to string
# float() = cast data from any type data to float

# num_str = input("Type a two digit number: ")
# digit1 = int(num_str[0])
# digit2 = int(num_str[1])
# print(digit1+digit2)

# a = float(200)
# print(type(a))
# print(a)

# print(60 + float("600.2"))

# print(str(100)  + str(300))
#num_char = len(input("Input Word(s) : "))
#print(type(num_char))

#new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")26

# 3. Mathematical operation
# ** = pangkat
# * = kali
# / = bagi

# print(3 * (3 + 3) / 3 - 3)
# height = input("Input your height(meter) : ")
# weight = input("Input your weight(kg) : ")

# print(int(float(weight) / (float(height) ** 2)))

# 4. Number manipulation and F Strings
# round() = rounded function to specify digit decimal number


# ========================== LIFE IN WEEKS ===========================
#  Create program using maths and f-String that tell us how many days,
#      weeks, months we have left if we live until 90 years old 
# 1 year = 365 days = 52 weeks = 12 months

# age = input("What is your current age?")

# ageINT = int(age)
# yearLeft = 90 - ageINT
# daysLeft = yearLeft * 365
# weeksLeft = yearLeft * 52
# monthsLeft = yearLeft * 12

# print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")

# ====================================================================

# ================ DAY 2 PROJECT - CALCULATOR TIP ====================
print("Welcome eto the tip calculator.")
totalBill = input("What was the total bill? $")
percenTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

pay = float(totalBill) * (float(percenTip) / 100)
pay = (pay + float(totalBill)) / float(people)

# print(f"Each person should pay: ${round(pay,2)}")

pay2 = "{:.2f}".format(pay)
print(f"Each person should pay2: ${pay2}")
# ====================================================================
