# digital_storage.py

units_digital_storage = {
    "Bit": 1,
    "Byte": 8,
    "Kilobit (Kb)": 1_000,
    "Kilobyte (KB)": 8_000,
    "Megabit (Mb)": 1_000_000,
    "Megabyte (MB)": 8_000_000,
    "Gigabit (Gb)": 1_000_000_000,
    "Gigabyte (GB)": 8_000_000_000,
    "Terabit (Tb)": 1_000_000_000_000,
    "Terabyte (TB)": 8_000_000_000_000,
    "Petabit (Pb)": 1_000_000_000_000_000,
    "Petabyte (PB)": 8_000_000_000_000_000,
    "Exabit (Eb)": 1_000_000_000_000_000_000,
    "Exabyte (EB)": 8_000_000_000_000_000_000
}

def convert_digital_storage(value, from_unit, to_unit):
    """Convert digital storage from one unit to another."""
    return (value * units_digital_storage[from_unit]) / units_digital_storage[to_unit]
