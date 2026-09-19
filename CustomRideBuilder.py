print("Step 1 : Pick your vehicle")
print(" 1 - bike")
print(" 2 - car")
print()
choice = int(input("Enter 1 or 2: "))
print()
if choice == 1 :
    print("Step 2 : Pick your bike type")
    print(" 1 - Scooty")
    print(" 2 - Mountain Bike")
    print()
    bike_type = int(input("Enter 1 or 2:"))
    if bike_type == 1 :
        print("You picked :  Scooty")
        print("Top speed  :  80km/h")
        print("Best for   :  City Roads")
    else:
        print("You picked :  Scooty")
        print("Top speed  :  80km/h")
        print("Best for   :  City Roads")
elif choice == 2 :
    print("Step 2 : Pick your car type")
    print(" 1 - Sedan")
    print(" 2 - SUV")
    print()
    car_type = int(input("Enter 1 or 2:"))
    if car_type == 1 :
        print("You picked :  Sedan")
        print("Seats  :  5 passengers")
        print("Best for   :  Family trips")
    else:
        print("You picked :  SUV")
        print("Seats  :  7 passengers")
        print("Best for   :  Off-Road Adventures")
else:
    print("Your choice isn't valid")
    print("Please enter 1 or 2 for a car or bike")
print()
print("Your custom ride is ready!")
print("Enjoy your journey!")
    