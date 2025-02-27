

units_time = {
    "Nanosecond": 1e-9,  # 1 ns = 10^-9 s
    "Microsecond": 1e-6,  # 1 µs = 10^-6 s
    "Millisecond": 1e-3,  # 1 ms = 10^-3 s
    "Second": 1,  # Base unit
    "Minute": 60,  # 1 min = 60 s
    "Hour": 3600,  # 1 hr = 3600 s
    "Day": 86400,  # 1 day = 86400 s
    "Week": 604800,  # 1 week = 604800 s
    "Month": 2.628e6,  # 1 month = ~2.628 million s (approx 30.44 days)
    "Calendar year": 3.154e7,  # 1 year = ~31.54 million s
    "Decade": 3.154e8,  # 1 decade = 10 years
    "Century": 3.154e9  # 1 century = 100 years
}

def convert_time(value, from_unit, to_unit):
    """Convert time from one unit to another."""
    return (value * units_time[from_unit]) / units_time[to_unit]
