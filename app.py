import math

z = 3 + 5j  # complex number


x = frozenset({"apple", "banana", "cherry"})

print(x)


print(10 / 3)
print(10 // 3)

print(round(2.8))
print(abs(2.9))


print(math.ceil(2.2))

#conditional statement
temperature = 10
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


#ternary operator
age = 10
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

#magic here---
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


# logical operator
high_income = True
good_credit = True
if high_income and good_credit:
    print("eLigible")
print("you aren't eligible for loan")
