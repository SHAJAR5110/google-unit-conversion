

units_fuel_economy = {
    "Miles per gallon (mpg)": 1,
    "Miles per gallon (UK) (mpg UK)": 1.20095,
    "Kilometers per liter (km/L)": 2.35215,
    "Liters per 100 km (L/100km)": 235.215
}

def convert_fuel_economy(value, from_unit, to_unit):
    """Convert fuel economy from one unit to another."""
    if from_unit == "Liters per 100 km (L/100km)":
        value = 235.215 / value  # Convert L/100km to mpg
        from_unit = "Miles per gallon (mpg)"

    if to_unit == "Liters per 100 km (L/100km)":
        return 235.215 / ((value * units_fuel_economy[from_unit]) / units_fuel_economy["Miles per gallon (mpg)"])
    
    return (value * units_fuel_economy[from_unit]) / units_fuel_economy[to_unit]
