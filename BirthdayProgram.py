import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

# Title
st.title("🎂 Age Calculator App")

# Ask user for birth date
birth_date = st.date_input("Enter your birth date:")

# Get today’s date
today = date.today()

if birth_date:
    if birth_date > today:
        st.error("❌ Birth date cannot be in the future!")
    else:
        # Calculate age
        age = relativedelta(today, birth_date)

        st.subheader("📅 Your Age Details:")
        st.write(f"**Current Date:** {today.strftime('%d-%m-%Y')}")
        st.write(f"**You are:** {age.years} years, {age.months} months, {age.days} days old.")
