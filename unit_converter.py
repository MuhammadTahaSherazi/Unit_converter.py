import streamlit as st

st.set_page_config(page_title="Google-like Unit Converter", page_icon="🔁")

st.title("🔁 Google Unit Converter")
st.write("Convert units easily, just like you would in Google!")

category = st.selectbox("Choose a category:", ["Length", "Weight", "Temperature"])

# Conversion logic
def convert_length(value, from_unit, to_unit):
    units = {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34
    }
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {
        "kilogram": 1,
        "pound": 0.453592
    }
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value
    else:
        return (value - 32) * 5/9 if to_unit == "Celsius" else value

# UI Logic
if category == "Length":
    from_unit = st.selectbox("From", ["meter", "kilometer", "mile"])
    to_unit = st.selectbox("To", ["meter", "kilometer", "mile"])
    value = st.number_input("Enter value:", 0.0)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["kilogram", "pound"])
    to_unit = st.selectbox("To", ["kilogram", "pound"])
    value = st.number_input("Enter value:", 0.0)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter value:", step=0.1)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")
