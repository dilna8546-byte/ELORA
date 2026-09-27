import streamlit as st

st.set_page_config(
    page_title="ELORA - BMI Calculator",
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
       NUMBER INPUT
       ========================= */

    .stNumberInput input {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5 !important;
        border-radius: 8px !important;
    }

    .stNumberInput button {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border-color: #D5D5D5 !important;
    }

    /* =========================
       BUTTON
       ========================= */

    .stButton > button {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #111111 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    .stButton > button p,
    .stButton > button span {
        color: #FFFFFF !important;
    }

    .stButton > button:hover {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #111111 !important;
    }

    .stButton > button:hover p,
    .stButton > button:hover span {
        color: #111111 !important;
    }

    /* =========================
       METRIC
       ========================= */

    [data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E2E2 !important;
        border-radius: 12px !important;
        padding: 18px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #555555 !important;
    }

    [data-testid="stMetricValue"] {
        color: #111111 !important;
    }

    /* =========================
       DIVIDERS
       ========================= */

    hr {
        border-color: #E0E0E0 !important;
    }

    /* =========================
       INFO BOX
       ========================= */

    [data-testid="stAlert"] {
        border-radius: 8px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# BMI CALCULATOR
# -----------------------------

st.title("BMI Calculator")

st.write(
    "Calculate Body Mass Index (BMI) using your height and weight."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=300.0,
        value=50.0,
        step=0.1
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=160.0,
        step=0.1
    )

if st.button("Calculate BMI", key="calculate_bmi"):

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.divider()

    st.subheader("Your BMI")

    st.metric(
        "BMI",
        f"{bmi:.1f}"
    )

    if bmi < 18.5:
        category = "Below the usual adult BMI range"
    elif bmi < 25:
        category = "Within the usual adult BMI range"
    elif bmi < 30:
        category = "Above the usual adult BMI range"
    else:
        category = "High adult BMI range"

    st.write(f"**Category:** {category}")

    st.info(
        "BMI is a general screening measure and does not diagnose health conditions. "
        "For children and teenagers, BMI should be interpreted using age- and sex-specific "
        "growth charts by a healthcare professional."
    )