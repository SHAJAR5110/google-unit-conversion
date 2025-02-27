
import math

units_plane_angle = {
    "Degree": 1,
    "Radian": math.pi / 180,
    "Gradian": 0.9,
    "Arcsecond": 1 / 3600,
    "Minute of arc": 1 / 60,
    "Milliradian": math.pi / 180 * 1000
}

def convert_plane_angle(value, from_unit, to_unit):
    """Convert plane angle from one unit to another."""
    return (value * units_plane_angle[from_unit]) / units_plane_angle[to_unit]
