#!/usr/bin/env python3
"""Simplified satellite pass prediction."""
import math

MU_EARTH = 3.986e14  # m^3/s^2
R_EARTH = 6371000  # meters

def orbital_velocity(altitude_km):
    r = R_EARTH + altitude_km * 1000
    return math.sqrt(MU_EARTH / r) / 1000  # km/s

def orbital_period(altitude_km):
    r = R_EARTH + altitude_km * 1000
    return 2 * math.pi * math.sqrt(r**3 / MU_EARTH) / 60  # minutes

def max_visible_distance(altitude_km):
    """Maximum distance satellite is visible from ground."""
    return math.sqrt(altitude_km * 1000 * 2 * R_EARTH) / 1000  # km

if __name__ == "__main__":
    sats = [("ISS", 420), ("Hubble", 540), ("GPS", 20200), ("Starlink", 550)]
    print("Satellite Pass Info")
    for name, alt in sats:
        v = orbital_velocity(alt)
        T = orbital_period(alt)
        d = max_visible_distance(alt)
        print(f"  {name:10s}: alt={alt}km, v={v:.1f}km/s, T={T:.1f}min, vis={d:.0f}km")\n