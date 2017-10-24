min = int(input("Enter min: "))

h = (min // 60) % 24
d = (min // 60) // 24
h_m = min % 60

print("Day:", d,"Hour:", h, "Minute:", h_m)