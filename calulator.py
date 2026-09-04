field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110
total = field1 + field2 + field3 + field4 + field5
average = total / 5
print ("total harvest     :", total, "kg")
print ("average per field     :", average, "kg")
price_per_kg = 15
earnings = total * price_per_kg
print("total esrnings     : Tk",earnings)
bags = total // 25
leftover = total % 25
print("full bags packed   :",bags)
print("leftover grains   :",leftover)
last_year = 500
print("better than last year?   :", total > last_year)
print("same as last year?   :", total == last_year)
print("at least as good?   :", total <= last_year)
total += 30
print("After bonus crop :", total, "kg")
total -= 15
print("After seed reserve :", total, "kg")
bags = total // 25
print("Final bags packed :", bags)