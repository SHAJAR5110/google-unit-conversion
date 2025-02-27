import streamlit as st
from length import convert_length, units_length
from area import convert_area, units_area
from dataTransfer import units_bit_transfer, convert_bit_transfer
from digital_storage import convert_digital_storage, units_digital_storage
from energy import convert_energy, units_energy
from frequency import convert_frequency, units_frequency
from fuel_economy import convert_fuel_economy, units_fuel_economy
from mass import convert_mass, units_mass
from plane_angle import convert_plane_angle, units_plane_angle
from pressure import convert_pressure, units_pressure
from speed import convert_speed, units_speed
from time_conversion import convert_time, units_time
from volume import convert_volume, units_volume

st.title("Unit Converter")

# Dropdown for choosing conversion type
conversion_type = st.selectbox("Choose conversion type:", ["Length","Volume","Area","Data Transfer","Digital Storage","Energy","Frequency","Fuel Economy","Mass","Plane Angle","Pressure","Speed","Time"])

if conversion_type == "Length":
    Convert_from = st.selectbox('From:', list(units_length.keys()))
    available_units = [unit for unit in units_length.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")

    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_length(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")

elif conversion_type == "Area":
    Convert_from = st.selectbox('From:', list(units_area.keys()))
    available_units = [unit for unit in units_area.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")

    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_area(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Data Transfer":
    Convert_from = st.selectbox('From:', list(units_bit_transfer.keys()))
    available_units = [unit for unit in units_bit_transfer.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")

    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_bit_transfer(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Digital Storage":
    Convert_from = st.selectbox('From:', list(units_digital_storage.keys()))
    available_units = [unit for unit in units_digital_storage.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")

    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_digital_storage(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Energy":
    Convert_from = st.selectbox('From:', list(units_energy.keys()))
    available_units = [unit for unit in units_energy.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")

    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_energy(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Frequency":
    Convert_from = st.selectbox('From:', list(units_frequency.keys()))
    available_units = [unit for unit in units_frequency.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_frequency(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Fuel Economy":
    Convert_from = st.selectbox('From:', list(units_fuel_economy.keys()))
    available_units = [unit for unit in units_fuel_economy.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_fuel_economy(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Mass":
    Convert_from = st.selectbox('From:', list(units_mass.keys()))
    available_units = [unit for unit in units_mass.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_mass(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Plane Angle":
    Convert_from = st.selectbox('From:', list(units_plane_angle.keys()))
    available_units = [unit for unit in units_plane_angle.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_plane_angle(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")                 
elif conversion_type == "Pressure":
    Convert_from = st.selectbox('From:', list(units_pressure.keys()))
    available_units = [unit for unit in units_pressure.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_pressure(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Speed":
    Convert_from = st.selectbox('From:', list(units_speed.keys()))
    available_units = [unit for unit in units_speed.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_speed(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")  
elif conversion_type == "Time":
    Convert_from = st.selectbox('From:', list(units_time.keys()))
    available_units = [unit for unit in units_time.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_time(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
elif conversion_type == "Volume":
    Convert_from = st.selectbox('From:', list(units_volume.keys()))
    available_units = [unit for unit in units_volume.keys() if unit != Convert_from]
    Convert_to = st.selectbox('To:', available_units)
    conversion_value = st.text_input('Enter the value to convert:', "1")
    
    if st.button("Convert"):
        try:
            value = float(conversion_value)
            result = convert_volume(value, Convert_from, Convert_to)
            st.success(f"{value} {Convert_from} = {result:.4f} {Convert_to}")
        except ValueError:
            st.error("Please enter a valid number.")
else:
    st.write("Please select a conversion type.") 
    