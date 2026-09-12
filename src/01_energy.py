GM = 398600.4418
def calculate_energy(velocity: float, altitude_km:float) -> float:
    r = 6371.0 + altitude_km
    energy = (velocity**2) / 2.0 - GM / r
    return energy

energy=calculate_energy(7.87,400)
print(energy)