temperature = int(input("Enter today's temperature in Celsius:"))
if temperature < 20:
    outfit = "jacket"
    print("It is cold today")
    print("Wear a ", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today")
    print("Wear a ", outfit)
is_raining =input("Is it raining today (yes/no):")
if is_raining == "yes":
    print("bring an umbrella")
wind_speed = int(input("Enter wind speed in km/h:"))
if wind_speed >30:
    needs_windbreaker = "yes"
    print("It is windy today")
    print("Wear a wind breaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("It is not windy today")
    print("You don't need to wear a wind breaker over your", outfit)
print("===== WEATHER OUTFIT PICKER =====")

print("Temperature:", temperature)

print("Outfit Chosen:", outfit)

print("Raining:", is_raining)

print("Windbreaker Needed:", needs_windbreaker)