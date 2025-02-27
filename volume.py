# volume.py

units_volume = {
    "US liquid gallon": 3.78541,  # 1 US gallon = 3.78541 liters
    "US liquid quart": 0.946353,  # 1 US quart = 0.946353 liters
    "US liquid pint": 0.473176,  # 1 US pint = 0.473176 liters
    "US legal cup": 0.24,  # 1 US legal cup = 0.24 liters
    "US fluid ounce": 0.0295735,  # 1 US fluid ounce = 0.0295735 liters
    "US tablespoon": 0.0147868,  # 1 US tablespoon = 0.0147868 liters
    "US teaspoon": 0.00492892,  # 1 US teaspoon = 0.00492892 liters
    "Cubic meter": 1000,  # 1 Cubic meter = 1000 liters
    "Liter": 1,  # Base unit
    "Milliliter": 0.001,  # 1 mL = 0.001 liters
    "Imperial gallon": 4.54609,  # 1 Imperial gallon = 4.54609 liters
    "Imperial quart": 1.13652,  # 1 Imperial quart = 1.13652 liters
    "Imperial pint": 0.568261,  # 1 Imperial pint = 0.568261 liters
    "Imperial cup": 0.284131,  # 1 Imperial cup = 0.284131 liters
    "Imperial fluid ounce": 0.0284131,  # 1 Imperial fluid ounce = 0.0284131 liters
    "Imperial tablespoon": 0.0177582,  # 1 Imperial tablespoon = 0.0177582 liters
    "Imperial teaspoon": 0.00591939,  # 1 Imperial teaspoon = 0.00591939 liters
    "Cubic foot": 28.3168,  # 1 Cubic foot = 28.3168 liters
    "Cubic inch": 0.0163871  # 1 Cubic inch = 0.0163871 liters
}

def convert_volume(value, from_unit, to_unit):
    """Convert volume from one unit to another."""
    return (value * units_volume[from_unit]) / units_volume[to_unit]
