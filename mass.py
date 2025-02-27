

units_mass = {
    "Tonne": 1_000,
    "Kilogram (kg)": 1,
    "Gram (g)": 0.001,
    "Milligram (mg)": 0.000001,
    "Microgram (µg)": 0.000000001,
    "Imperial ton": 1_016.05,
    "US ton": 907.184,
    "Stone": 6.35029,
    "Pound (lb)": 0.453592,
    "Ounce (oz)": 0.0283495
}

def convert_mass(value, from_unit, to_unit):
    """Convert mass from one unit to another."""
    return (value * units_mass[from_unit]) / units_mass[to_unit]
