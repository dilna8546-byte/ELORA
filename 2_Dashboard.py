import streamlit as st
from elora_theme import apply_elora_theme

st.set_page_config(
    page_title="ELORA - Dashboard",
    page_icon="🌿",
    layout="wide"
)

apply_elora_theme()

# -----------------------------
# DASHBOARD HEADER
# -----------------------------

st.markdown(
    """
    <div style="text-align:center; padding:20px 10px 10px 10px;">
        <h1>ELORA</h1>
        <h2>Your Health & Nutrition Dashboard</h2>
        <p style="font-size:17px;">
            Explore personalized nutrition and health tools.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# PERSONALIZED HEALTH
# -----------------------------

st.subheader("Personalized Health")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Personalized Diet")
    st.write("Nutrition guidance based on your health condition.")

    if st.button("Open", key="dashboard_diet"):
        st.switch_page("pages/5_Personalized_Diet.py")

with col2:
    st.markdown("### Disease Meal Plans")
    st.write("Explore meal plans for different health conditions.")

    if st.button("Open", key="dashboard_meal_plans"):
        st.switch_page("pages/7_Disease_Meal_Plans.py")

with col3:
    st.markdown("### Smart Recommendations")
    st.write("Get food recommendations using nutrition rules.")

    if st.button("Open", key="dashboard_recommendations"):
        st.switch_page("pages/8_Smart_Recommendations.py")


st.divider()

# -----------------------------
# FOOD & NUTRITION
# -----------------------------

st.subheader("Food & Nutrition")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Food Nutrition")
    st.write("Explore nutritional information for different foods.")

    if st.button("Open", key="dashboard_food"):
        st.switch_page("pages/4_Food_Nutrition.py")

with col2:
    st.markdown("### Healthy Recipes")
    st.write("Find healthy recipes for everyday meals.")

    if st.button("Open", key="dashboard_recipes"):
        st.switch_page("pages/6_Healthy_Recipes.py")

with col3:
    st.markdown("### Baby Meal Planner")
    st.write("Explore age-appropriate baby meal guidance.")

    if st.button("Open", key="dashboard_baby"):
        st.switch_page("pages/3_Baby_Meal_Planner.py")


st.divider()

# -----------------------------
# HEALTH TOOLS
# -----------------------------

st.subheader("Health Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### BMI Calculator")
    st.write("Calculate BMI for general informational purposes.")

    if st.button("Open", key="dashboard_bmi"):
        st.switch_page("pages/10_BMI_Calculator.py")

with col2:
    st.markdown("### Water Intake Tracker")
    st.write("Keep track of your daily water intake.")

    if st.button("Open", key="dashboard_water"):
        st.switch_page("pages/11_Water_Intake_Tracker.py")

with col3:
    st.markdown("### Track Recovery")
    st.write("Record your daily wellness progress.")

    if st.button("Open", key="dashboard_recovery"):
        st.switch_page("pages/13_Track_Recovery.py")


st.divider()

# -----------------------------
# ASSISTANT & PROFILE
# -----------------------------

st.subheader("Assistant & Profile")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### AI Health Chatbot")
    st.write("Ask questions about food and nutrition.")

    if st.button("Open", key="dashboard_chatbot"):
        st.switch_page("pages/9_AI_Health_Chatbot.py")

with col2:
    st.markdown("### My Profile")
    st.write("Manage your nutrition and wellness preferences.")

    if st.button("Open", key="dashboard_profile"):
        st.switch_page("pages/12_Profile.py")