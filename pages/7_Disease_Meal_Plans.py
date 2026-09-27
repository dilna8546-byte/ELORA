import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ELORA - Disease Meal Plans",
    page_icon="",
    layout="wide"
)

# -----------------------------
# ELORA BLACK & WHITE THEME
# -----------------------------

st.markdown(
    """
    <style>

    /* =========================
       MAIN BACKGROUND
       ========================= */

    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background-color: #F7F7F7 !important;
        color: #111111 !important;
    }

    /* =========================
       HEADINGS & TEXT
       ========================= */

    h1, h2, h3, h4, h5, h6 {
        color: #111111 !important;
    }

    p,
    label,
    span,
    .stMarkdown {
        color: #222222 !important;
    }

    /* =========================
       SIDEBAR
       ========================= */

    [data-testid="stSidebar"] {
        background-color: #111111 !important;
    }

    [data-testid="stSidebar"] > div {
        background-color: #111111 !important;
    }

    [data-testid="stSidebarNav"] {
        background-color: #111111 !important;
    }

    [data-testid="stSidebarNav"] ul {
        background-color: #111111 !important;
    }

    [data-testid="stSidebarNav"] li {
        background-color: #111111 !important;
    }

    [data-testid="stSidebarNav"] a {
        background-color: #111111 !important;
        color: #FFFFFF !important;
    }

    [data-testid="stSidebarNav"] a span {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    [data-testid="stSidebarNav"] a div {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebarNav"] a p {
        color: #FFFFFF !important;
    }

    /* Selected page */

    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background-color: #2A2A2A !important;
        color: #FFFFFF !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] span,
    [data-testid="stSidebarNav"] a[aria-current="page"] div,
    [data-testid="stSidebarNav"] a[aria-current="page"] p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    /* Hover */

    [data-testid="stSidebarNav"] a:hover {
        background-color: #222222 !important;
        color: #FFFFFF !important;
    }

    [data-testid="stSidebarNav"] a:hover span,
    [data-testid="stSidebarNav"] a:hover div,
    [data-testid="stSidebarNav"] a:hover p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    /* =========================
       SELECT BOX
       ========================= */

    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5 !important;
        border-radius: 8px !important;
    }

    [data-testid="stSelectbox"] div[data-baseweb="select"] * {
        color: #111111 !important;
    }

    /* =========================
       DROPDOWN MENU
       ========================= */

    [data-baseweb="popover"] {
        background-color: #FFFFFF !important;
    }

    [role="option"] {
        background-color: #FFFFFF !important;
        color: #111111 !important;
    }

    [role="option"]:hover {
        background-color: #F0F0F0 !important;
        color: #111111 !important;
    }

    /* =========================
       DIVIDERS
       ========================= */

    hr {
        border-color: #E0E0E0 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# LOAD DATA
# -----------------------------

disease_meal_plans = pd.read_excel(
    "Disease-Based Meal Plans Dataset.xlsx"
)

disease_meal_plans = disease_meal_plans.dropna(how="all")

# -----------------------------
# DISEASE MEAL PLANS
# -----------------------------

st.title("Disease Meal Plans")

st.write(
    "Explore meal ideas and nutrition guidance "
    "for different health conditions."
)

st.divider()

meal_diseases = (
    disease_meal_plans["Disease/Condition"]
    .dropna()
    .astype(str)
    .str.strip()
    .drop_duplicates()
    .tolist()
)

selected_disease = st.selectbox(
    "Choose a health condition:",
    ["Select a condition"] + meal_diseases,
    key="meal_plan_condition_page"
)

if selected_disease != "Select a condition":

    meal_plan = disease_meal_plans[
        disease_meal_plans["Disease/Condition"]
        .astype(str)
        .str.strip()
        == selected_disease.strip()
    ]

    if not meal_plan.empty:

        meal = meal_plan.iloc[0]

        st.divider()

        st.subheader(
            f"Meal Plan for {selected_disease}"
        )

        st.markdown("### Breakfast")
        st.write(meal["Breakfast"])

        st.markdown("### Lunch")
        st.write(meal["Lunch"])

        st.markdown("### Dinner")
        st.write(meal["Dinner"])

        st.markdown("### Snack")
        st.write(meal["Snack"])

        st.markdown("### Hydration Advice")
        st.write(meal["Hydration Advice"])

        st.markdown("### Reason / Health Goal")
        st.write(meal["Reason/Health Goal"])

        st.markdown("### Recommended Foods")
        st.write(meal["Recommended Foods"])

        st.markdown("### Foods to Limit/Avoid")
        st.write(meal["Foods to Limit/Avoid"])

        st.markdown("### Source")
        st.write(meal["Source"])