# core/orbital.py - Toolkit Orbital Portafolio R
import math
import numpy as np

GM = 398600.4418  # km3/s2
R_EARTH = 6371.0  # km

def orbital_velocity(alt_km: float | np.ndarray) -> float | np.ndarray:
    """Circular speed v = sqrt(GM/r)"""
    r = R_EARTH + alt_km
    return np.sqrt(GM / r)

def escape_velocity(alt_km: float) -> float:
    """escape velocity v esc = sqrt(2 GM/r)"""
    r = R_EARTH + alt_km
    return math.sqrt(2 * GM / r)

def orbital_period(alt_km: float) -> float:
    """Orbital period in minutes"""
    r = R_EARTH + alt_km
    T_sec = 2 * math.pi * math.sqrt(r**3 / GM)
    return T_sec / 60.0