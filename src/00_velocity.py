import math

GM = 398600.4418 #Standard gravitational parameter of the Earth, Gravitational Constant * Earth Mass

def circular_velocity(altitude_km: float) -> float:
    """
    Calcula velocidad para órbita circular
    """
    r = 6371.0 + altitude_km #Radius of the Earth plus the height
    return math.sqrt(GM / r)

# --- TESTS ---
# No los modifiques, tu función debe pasarlos
#assert abs(velocidad_circular(400) - 7.67) < 0.05, "Falló ISS"
#assert abs(velocidad_circular(2000) - 6.9) < 0.05, "Falló tu límite 2000km"
#assert velocidad_circular(0) > velocidad_circular(400), "A menor altitud, mayor velocidad"
#print("✅ Nivel 0.1 PASADO - Ya sabes calcular velocidad orbital")

