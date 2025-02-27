

units_energy = {
    "Joule (J)": 1,
    "Kilojoule (kJ)": 1_000,
    "Calorie (cal)": 4.184,
    "Kilocalorie (kcal)": 4_184,
    "Watt-hour (Wh)": 3_600,
    "Kilowatt-hour (kWh)": 3_600_000,
    "Electronvolt (eV)": 1.60218e-19,
    "British thermal unit (BTU)": 1_055.06,
    "Foot-pound (ft-lb)": 1.35582
}

def convert_energy(value, from_unit, to_unit):
    """Convert energy from one unit to another."""
    return (value * units_energy[from_unit]) / units_energy[to_unit]
