import streamlit as st

st.set_page_config(
    page_title="ELORA - Water Intake Tracker",
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
       METRIC CARD
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
       ALERTS
       ========================= */

    [data-testid="stAlert"] {
        border-radius: 8px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# WATER INTAKE TRACKER
# -----------------------------

st.title("Water Intake Tracker")

st.write(
    "Track your water intake and learn about healthy hydration habits."
)

st.divider()

water = st.number_input(
    "Water consumed today (ml)",
    min_value=0,
    max_value=10000,
    value=0,
    step=250
)

if st.button("Check Hydration", key="check_hydration"):

    st.divider()

    st.subheader("Today's Water Intake")

    st.metric(
        "Water consumed",
        f"{water:,} ml"
    )

    st.write(
        "Regular hydration is important for normal body functions. "
        "Water needs vary depending on age, activity, weather, diet, "
        "and individual health needs."
    )

    if water == 0:
        st.info(
            "No water intake has been entered yet. "
            "Use the tracker to record what you drink."
        )
    else:
        st.success(
            "Your water intake has been recorded for this session."
        )

st.divider()

st.info(
    "This tracker is for general educational purposes. "
    "Individual fluid needs vary, and medical conditions may require "
    "specific hydration advice from a healthcare professional."
)