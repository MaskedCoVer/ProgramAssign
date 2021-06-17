grocerylist_price = {"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.00, "Milk": 2.50}
icecream_price = {"mintcc": 2.00, "ube": 3.00, "choco": 1.50, "strawberry":1.00}

ube_price = icecream_price["ube"]
mintcc_price = icecream_price["mintcc"]
choco_price = icecream_price["choco"]
strawberry_price = icecream_price["strawberry"]

print(ube_price)

Chicken_price = grocerylist_price["Chicken"]
Beef_price = grocerylist_price["Beef"]
Cheese_price = grocerylist_price["Cheese"]
Milk_price = grocerylist_price["Milk"]

icecream_price["ube"]+= 0.50
print(ube_price)

shoe_inventory = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
dunks_inv = shoe_inventory["SB Dunk"]
dunks_inv -= 2
yeezy_inv = shoe_inventory["Yeezy"]
yeezy_inv += 1
jordan_inv = shoe_inventory["Jordan 13"]
air_inv = shoe_inventory["Air Max"]

dunks_inv += 7
yeezy_inv += 7
jordan_inv += 7
air_inv += 7

dunks_inv -= 3
yeezy_inv -= 3
jordan_inv -= 3
air_inv -= 3

grocerylist_price["Eggs"] = 4.50
icecream_price["Vanilla"] = 2.55
shoe_inventory["Converse"] = 4

del grocerylist_price["Beef"]
del icecream_price["mintcc"]

print(grocerylist_price)
print(icecream_price)
print(shoe_inventory)


