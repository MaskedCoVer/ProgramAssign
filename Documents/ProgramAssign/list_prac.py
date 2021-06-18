US_cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(US_cities)

bag_contents = ["tissues", "sanitizer", "chapstick", "wipes", "water", "gum", "keys", "wallet", "mask", "phone"]
print(bag_contents)

print(US_cities[0])
print(US_cities[-3])
print(US_cities[2])

print(bag_contents[9])
print(bag_contents[3])
print(bag_contents[-2])

four_cities = US_cities[1:4]
shopping_list = bag_contents[0:3]

US_cities[0] = "San Francisco"
US_cities[2] = "Brooklyn"
US_cities[7] = "Hollywood"
US_cities[5] = "Tampa"
print(US_cities)

US_cities.append("Oakland")
US_cities.extend(["New York City", "Los Angeles"])
US_cities.insert(0, "Miami")
print(US_cities)

del US_cities[1]
US_cities.pop(5)
US_cities.remove("Denver")
print(US_cities)