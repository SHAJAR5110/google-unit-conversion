

units_speed = {
    "Mile per hour (mph)": 0.44704,  # 1 mph = 0.44704 m/s
    "Foot per second (ft/s)": 0.3048,  # 1 ft/s = 0.3048 m/s
    "Metre per second (m/s)": 1,  # Base unit
    "Kilometre per hour (km/h)": 0.277778,  # 1 km/h = 0.277778 m/s
    "Knot (kn)": 0.514444  # 1 knot = 0.514444 m/s
}

def convert_speed(value, from_unit, to_unit):
    """Convert speed from one unit to another."""
    return (value * units_speed[from_unit]) / units_speed[to_unit]
