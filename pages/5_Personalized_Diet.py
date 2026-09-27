import streamlit as st
import pandas as pd
from elora_theme import apply_elora_theme

st.set_page_config(
    page_title="ELORA - Personalized Diet",
    page_icon="🌿",
    layout="wide"
)

apply_elora_theme()

# -----------------------------
# LOAD DISEASE NUTRITION DATA
# -----------------------------

disease_nutrition = pd.read_excel(
    "Disease-Based Nutrition Dataset.xlsx"
)

disease_nutrition = disease_nutrition.dropna(how="all")

# -----------------------------
# PERSONALIZED DIET
# -----------------------------

st.title("Personalized Diet")

st.write(
    "Get nutrition guidance based on your selected "
    "health condition."
)

st.divider()

disease_list = (
    disease_nutrition["Disease/Condition"]
    .dropna()
    .astype(str)
    .str.strip()
    .drop_duplicates()
    .tolist()
)

selected_disease = st.selectbox(
    "Choose a health condition:",
    ["Select a condition"] + disease_list,
    key="diet_condition_page"
)

# -----------------------------
# SHOW DIET PLAN
# -----------------------------

if selected_disease != "Select a condition":

    diet = disease_nutrition[
        disease_nutrition["Disease/Condition"]
        .astype(str)
        .str.strip()
        == selected_disease
    ].iloc[0]

    st.divider()

    st.subheader(
        f"Nutrition Guidance for {selected_disease}"
    )

    st.markdown("### Recommended Foods")
    st.write(diet["Recommended Foods"])

    st.markdown("### Foods to Limit/Avoid")
    st.write(diet["Foods to Limit/Avoid"])

    st.markdown("### Key Nutrients Needed")
    st.write(diet["Key Nutrients Needed"])

    st.markdown("### Nutrition Benefits")
    st.write(diet["Nutrition Benefits"])

    st.markdown("### Meal Suggestions")
    st.write(diet["Meal Suggestions"])

    st.markdown("### Source")
    st.write(diet["Source"])

    # -----------------------------
    # SAVE DIET PLAN
    # -----------------------------

    st.divider()

    st.subheader("Save Diet Plan")

    if st.button("Save Diet Plan", key="save_diet_plan"):

        st.session_state["saved_diet_plan"] = {
            "Disease/Condition": selected_disease,
            "Recommended Foods": diet["Recommended Foods"],
            "Foods to Limit/Avoid": diet["Foods to Limit/Avoid"],
            "Key Nutrients Needed": diet["Key Nutrients Needed"],
            "Nutrition Benefits": diet["Nutrition Benefits"],
            "Meal Suggestions": diet["Meal Suggestions"],
            "Source": diet["Source"]
        }

        st.success("Diet plan saved successfully!")

# -----------------------------
# DISPLAY SAVED DIET PLAN
# -----------------------------

if "saved_diet_plan" in st.session_state:

    st.divider()

    st.subheader("Saved Diet Plan")

    saved_plan = st.session_state["saved_diet_plan"]

    st.write(
        f"**Health Condition:** "
        f"{saved_plan['Disease/Condition']}"
    )

    st.markdown("### Recommended Foods")
    st.write(saved_plan["Recommended Foods"])

    st.markdown("### Foods to Limit/Avoid")
    st.write(saved_plan["Foods to Limit/Avoid"])

    st.markdown("### Key Nutrients Needed")
    st.write(saved_plan["Key Nutrients Needed"])

    st.markdown("### Nutrition Benefits")
    st.write(saved_plan["Nutrition Benefits"])

    st.markdown("### Meal Suggestions")
    st.write(saved_plan["Meal Suggestions"])

    st.success("Your diet plan is saved for this ELORA session.")