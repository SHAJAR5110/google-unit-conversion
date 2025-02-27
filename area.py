
units_area = {
    "Square kilometre": 1_000_000,  
    "Square metre": 1,              
    "Square mile": 2_589_988,       
    "Square yard": 0.836127,        
    "Square foot": 0.092903,        
    "Square inch": 0.00064516,      
    "Hectare": 10_000,              
    "Acre": 4046.86                 
}

def convert_area(value, from_unit, to_unit):
    """Convert area from one unit to another."""
    return (value * units_area[from_unit]) / units_area[to_unit]
