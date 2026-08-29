name = input("enter your name:")
gadget = input("enter your favourite gadget:")
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True
print("Name", name, "-> type:", type(name))
print("Gadget", gadget, "-> type:", type(gadget))
print("agent_number", agent_number, "-> type:", type(agent_number))
print("speed_rating", speed_rating, "-> type:", type(speed_rating))
print("mission_count", mission_count, "-> type:", type(mission_count))
print("height_m", height_m, "-> type:", type(height_m))
print("is_active", is_active, "-> type:", type(is_active))
agent_number_text = str(agent_number)
mission_count_text = str(agent_number)
speed_rating_text = str(agent_number)
status_text = str(is_active)
print("agent number as text", agent_number, "-> type:", type(agent_number))
print("mission count as text", mission_count, "-> type:", type(mission_count))
print("speed rating as text", speed_rating, "-> type:", type(speed_rating))
print("status as text ", status_text, "-> type:", type(status_text))
first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter