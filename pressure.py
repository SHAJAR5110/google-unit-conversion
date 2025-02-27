

units_pressure = {
    "Bar": 100000,  # 1 Bar = 100000 Pascals
    "Pascal (Pa)": 1,
    "Pound per square inch (psi)": 6894.76,  # 1 psi = 6894.76 Pascals
    "Standard atmosphere (atm)": 101325,  # 1 atm = 101325 Pascals
    "Torr": 133.322  # 1 Torr = 133.322 Pascals
}

def convert_pressure(value, from_unit, to_unit):
    """Convert pressure from one unit to another."""
    return (value * units_pressure[from_unit]) / units_pressure[to_unit]
