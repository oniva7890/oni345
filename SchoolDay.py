weather = input("(sunny/rainy/cloudy)").strip().lower()
homework =input("(yes/no)").strip().lower()
day = input("(Monday to Sunday)").strip().capitalize()
print()
if day in ("Saturday", "Sunday") :
    print("Daytype     : WEEKEND; Enjoy your free time")
elif day== "Monday" :
     print("Daytype     : FIRST DAY OF THE WEEK; Pack your weekly planner")
elif day== ("Tuesday", "Wednesday" , "Thursday") :
     print("Daytype     : REGULAR SCHOOL DAY; stay focused")
elif day== "Friday" :
     print("Daytype     : END OF THE WEEK; You can finally rest")
else :
     print("Day not recognized, Please check the spelling")
if weather == "sunny" and homework == "yes":
print("After school: Head to the park - great weather and homework is done!")
# Topic 3 -- OR operator: rainy OR cloudy
if weather == "rainy" or weather == "cloudy":
print("Weather tip : Pack your umbrella - it may get wet outside.")