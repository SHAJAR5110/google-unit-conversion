
units_length = {
    "Kilometre": 1000,
    "Metre": 1,
    "Centimetre": 0.01,
    "Millimetre": 0.001,
    "Micrometre": 1e-6,
    "Nanometre": 1e-9,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Nautical mile": 1852
}

def convert_length(value, from_unit, to_unit):
    """Convert length from one unit to another."""
    return (value * units_length[from_unit]) / units_length[to_unit]
