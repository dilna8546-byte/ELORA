import streamlit as st

from theme import apply_elora_theme

st.set_page_config(
    page_title="ELORA - Profile",
    page_icon="🌿",
    layout="wide"
)

apply_elora_theme()

st.title("My Profile")
st.write("Tell ELORA about your nutrition and wellness preferences.")

st.divider()

# PERSONAL INFORMATION

st.subheader("Personal Information")

name = st.text_input(
    "Name",
    placeholder="Enter your name"
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=18,
    step=1
)

# HEALTH & NUTRITION

st.subheader("Health & Nutrition")

health_goal = st.selectbox(
    "Main health goal",
    [
        "Select a goal",
        "Healthy eating",
        "Balanced nutrition",
        "Managing a health condition",
        "Baby nutrition",
        "General wellness"
    ]
)

dietary_preference = st.selectbox(
    "Dietary preference",
    [
        "Not specified",
        "Vegetarian",
        "Non-vegetarian",
        "Vegan",
        "Eggetarian"
    ]
)

allergy = st.selectbox(
    "Food allergy",
    [
        "None",
        "Nuts",
        "Dairy",
        "Eggs",
        "Fish",
        "Shellfish",
        "Gluten",
        "Other"
    ]
)

health_condition = st.selectbox(
    "Health condition",
    [
        "None",
        "Diabetes",
        "Hypertension",
        "Heart-related condition",
        "Obesity",
        "Other"
    ]
)

st.divider()

# SAVE PROFILE

if st.button("Save Profile"):

    st.session_state["profile"] = {
        "Name": name,
        "Age": age,
        "Health Goal": health_goal,
        "Dietary Preference": dietary_preference,
        "Food Allergy": allergy,
        "Health Condition": health_condition
    }

    st.success("Profile saved successfully!")

# DISPLAY SAVED PROFILE

if "profile" in st.session_state:

    st.divider()

    st.subheader("Your Profile")

    profile = st.session_state["profile"]

    st.write(f"**Name:** {profile['Name']}")
    st.write(f"**Age:** {profile['Age']}")
    st.write(f"**Health Goal:** {profile['Health Goal']}")
    st.write(f"**Dietary Preference:** {profile['Dietary Preference']}")
    st.write(f"**Food Allergy:** {profile['Food Allergy']}")
    st.write(f"**Health Condition:** {profile['Health Condition']}")

    st.success("Your preferences are saved for this ELORA session.")