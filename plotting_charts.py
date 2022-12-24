import csv
import matplotlib.pyplot as plt

rows = []

with open("data.csv", "r", encoding="UTF-8") as f:
  reader = csv.reader(f)

  for row in reader:
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]

names = []
masses = []
radiuses = []
gravity = []

for planet_data in planet_data_rows:
  if len(planet_data) == 13:
    names.append(planet_data[1])
    masses.append(planet_data[3])
    radiuses.append(planet_data[4])
    gravity.append(planet_data[12])

masses.sort()
radiuses.sort()
gravity.sort()


plt.plot(radiuses, masses)
plt.title("Planet Radius vs Mass")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(masses, gravity)
plt.title("Planet Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()