#nakakalito

sender_name = input("Enter sender name:")
item = input("Type of the Item:")

fragile_input = input("Is the item fragile?:")
isFragile = bool(fragile_input == "yes" or fragile_input == "Yes")

if isFragile == True:
    print("Noted, the item is fragile.")
else:
    print("Noted, the item is not fragile.")

weight = float(input("Weight of the item KG:"))
distance = float(input("Destination in KM?:"))

express_input = input("Is it Express?:")
is_express = bool(express_input == "yes" or express_input == "Yes")

intl_input = input("Is it international?:")
is_international = bool(intl_input == "yes" or intl_input == "Yes")

print("Weight KG:", weight)
print("Distance KM:", distance)

if is_express == True:
    print("Express: True")
else:
    print("Express: False")

if is_international == True:
    print("International: True")
else:
    print("International: False")

base_cost = weight*2.5 + distance*0.15

if weight <= 2.0 and distance <= 100 and is_express == False and is_international == False:
    total = 0.00
elif is_international == True and is_express == True:
    total = (base_cost * 1.40) + 50
elif is_express == True or (is_international == True and weight > 20):
    total = (base_cost * 1.20) + 25
elif weight > 30 or distance > 1000:
    total = base_cost + 30
else:
    total = base_cost

print("Expected output:", total)