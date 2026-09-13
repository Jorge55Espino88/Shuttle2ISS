import math
import matplotlib.pyplot as plt

GM = 398600.4418
R_EARTH = 6371.0

def orbital_velocity(alt):
    return math.sqrt(GM / (R_EARTH + alt))

altitudes = [200, 300, 400, 500, 1000, 2000]
velocities = [orbital_velocity(a) for a in altitudes]

plt.plot(altitudes, velocities, marker='o')
plt.xlabel("Altitude km")
plt.ylabel("Speed km/s")
plt.title("Why higher = slower")
plt.grid(True)
plt.show()