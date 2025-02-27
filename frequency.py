

units_frequency = {
    "Hertz (Hz)": 1,
    "Kilohertz (kHz)": 1_000,
    "Megahertz (MHz)": 1_000_000,
    "Gigahertz (GHz)": 1_000_000_000,
    "Terahertz (THz)": 1_000_000_000_000,
    "Revolutions per second (RPS)": 1,
    "Revolutions per minute (RPM)": 1 / 60,
    "Beats per minute (BPM)": 1 / 60
}

def convert_frequency(value, from_unit, to_unit):
    """Convert frequency from one unit to another."""
    return (value * units_frequency[from_unit]) / units_frequency[to_unit]
