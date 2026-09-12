import math

GM = 398600.4418

def calculate_escape_velocity(altitude_km:float) -> float:
    r = 6371.0 + altitude_km
    escape_velocity = math.sqrt(2*GM/r)
    return escape_velocity

speed = calculate_escape_velocity(0)
print(f"Speed 0 km: {speed}")
speed = calculate_escape_velocity(400)
print(f"Speed 400 km: {speed}")