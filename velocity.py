import matplotlib.pyplot as plt
import numpy as np
from core.orbital import orbital_velocity

alts = np.linspace(200, 2000, 1000)
vels = orbital_velocity(alts)

plt.plot(alts, vels)
plt.xlabel("Altitude (km)")
plt.ylabel("Speed (km/s)")
plt.title("Level 0.4 - Speed vs Altitude")
plt.savefig("docs/velocity_curve.png", dpi=150)
plt.show()