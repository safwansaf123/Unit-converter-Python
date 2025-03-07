import streamlit as st  # Import Streamlit for creating the web-based UI


# Function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {

        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
        "kilometers_miles": 0.621371,
        "miles_kilometers": 1 / 0.621371,
        "kilogram_pounds": 2.20462,
        "pounds_kilogram": 1 / 2.20462,
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
        "liters_gallons": 0.264172,
        "gallons_liters": 1 / 0.264172,
         "ml_fl_ounces": 0.033814,
        "fl_ounces_ml": 1 / 0.033814,

    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function (e.g., temperature conversion), call it
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Otherwise, multiply by the conversion factor
    else:
        return "Conversion not supported"  # Return message if conversion is not defined


# Streamlit UI setup
# Apply CSS styles for the title
st.title("Simple Unit Converter")  # Set title for the web app

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms", "miles", "pounds", "celsius", "fahrenheit", "liters", "gallons", "fl_ounces", "ml"]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms", "miles", "pounds", "celsius", "fahrenheit", "liters", "gallons", "fl_ounces", "ml"])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    st.write(f"Converted Value: {result}")  # Display the result