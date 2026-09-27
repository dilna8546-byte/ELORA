import streamlit as st
import pandas as pd
from elora_theme import apply_elora_theme

# -----------------------------
# ELORA BABY MEAL PLANNER THEME
# -----------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #F3EBDD;
        color: #171512;
    }

    h1, h2, h3 {
        color: #171512 !important;
    }

    p, label, .stMarkdown {
        color: #171512 !important;
    }

    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFDF8;
        color: #171512;
    }

    hr {
        border-color: #D6C8B5;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="ELORA - Baby Meal Planner",
    page_icon="👶",
    layout="wide"
)

apply_elora_theme()

baby_meal_planner = pd.read_excel(
    "Baby Meal Planner Dataset.xlsx"
)

baby_meal_planner = baby_meal_planner.dropna(how="all")

st.title("Baby Meal Planner")

st.write(
    "Explore age-appropriate nutrition information "
    "for babies."
)

st.divider()

baby_age_groups = (
    baby_meal_planner["Age Group"]
    .dropna()
    .astype(str)
    .str.strip()
    .drop_duplicates()
    .tolist()
)

selected_baby_age = st.selectbox(
    "Select baby's age group:",
    ["Select an age group"] + baby_age_groups,
    key="baby_age_group_page"
)

if selected_baby_age != "Select an age group":

    baby_info = baby_meal_planner[
        baby_meal_planner["Age Group"]
        .astype(str)
        .str.strip()
        == selected_baby_age.strip()
    ]

    if not baby_info.empty:

        st.markdown("### Recommended Foods")

        for food in baby_info["Recommended Foods"].dropna().astype(str).unique():
            st.write(f"• {food}")

        st.markdown("### Foods to Avoid/Limit")

        for food in baby_info["Foods to Avoid/Limit"].dropna().astype(str).unique():
            st.write(f"• {food}")

        st.markdown("### Key Nutrients Needed")

        for nutrient in baby_info["Key Nutrients Needed"].dropna().astype(str).unique():
            st.write(f"• {nutrient}")

        st.markdown("### Nutrition Benefits")

        for benefit in baby_info["Nutrition Benefits"].dropna().astype(str).unique():
            st.write(f"• {benefit}")

        st.markdown("### Meal Suggestions")

        for meal in baby_info["Meal Suggestions"].dropna().astype(str).unique():
            st.write(f"• {meal}")

        st.markdown("### Source")

        st.write(
            " • ".join(
                baby_info["Source"]
                .dropna()
                .astype(str)
                .unique()
            )
        )