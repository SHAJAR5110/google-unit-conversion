

units_bit_transfer = {
    "Bits per second (bps)": 1,
    "Kilobits per second (Kbps)": 1_000,
    "Megabits per second (Mbps)": 1_000_000,
    "Gigabits per second (Gbps)": 1_000_000_000,
    "Terabits per second (Tbps)": 1_000_000_000_000,
    "Bytes per second (Bps)": 8,
    "Kilobytes per second (KBps)": 8_000,
    "Megabytes per second (MBps)": 8_000_000,
    "Gigabytes per second (GBps)": 8_000_000_000,
    "Terabytes per second (TBps)": 8_000_000_000_000
}

def convert_bit_transfer(value, from_unit, to_unit):
    """Convert data transfer rate from one unit to another."""
    return (value * units_bit_transfer[from_unit]) / units_bit_transfer[to_unit]
