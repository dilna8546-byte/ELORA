import streamlit as st

st.set_page_config(
    page_title="ELORA - Health & Nutrition",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# ELORA BLACK & WHITE HOME
# ==============================

st.markdown(
    """
    <style>

    /* =========================
       MAIN BACKGROUND
       ========================= */

    .stApp {
        background-color: #F7F7F7;
        color: #111111;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 4rem;
        padding-bottom: 3rem;
    }

    /* =========================
       TEXT
       ========================= */

    h1, h2, h3, h4 {
        color: #111111 !important;
    }

    p {
        color: #4A4A4A;
    }

    /* =========================
       BLACK BUTTONS
       ========================= */

    .stButton > button {
        background-color: #111111;
        color: #FFFFFF !important;
        border: 1px solid #111111;
        border-radius: 10px;
        padding: 0.65rem 1.5rem;
        font-size: 16px;
        font-weight: 500;
        transition: 0.2s ease;
    }

    .stButton > button p {
        color: #FFFFFF !important;
    }

    .stButton > button:hover {
        background-color: #FFFFFF;
        color: #111111 !important;
        border: 1px solid #111111;
    }

    .stButton > button:hover p {
        color: #111111 !important;
    }

    /* =========================
       DIVIDERS
       ========================= */

    hr {
        border-color: #E0E0E0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# BRAND
# ==============================

st.markdown(
    """
    <h1 style="
        text-align:center;
        font-size:60px;
        letter-spacing:7px;
        color:#111111;
        margin-bottom:0;
    ">
        ELORA
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:17px;
        color:#666666;
        margin-top:5px;
        letter-spacing:1px;
    ">
        Personalized Health & Nutrition
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ==============================
# HERO
# ==============================

st.markdown(
    """
    <h2 style="
        text-align:center;
        font-size:38px;
        line-height:1.25;
        color:#111111;
    ">
        AI-Powered Personalized<br>
        Health & Nutrition Assistant
    </h2>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        width:55px;
        height:2px;
        background:#111111;
        margin:28px auto;
    "></div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:21px;
        font-weight:500;
        color:#2F2F2F;
    ">
        Understand your nutrition. Make better choices.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        max-width:700px;
        margin:18px auto;
        font-size:16px;
        line-height:1.8;
        color:#555555;
    ">
        ELORA brings personalized nutrition guidance, food insights,
        meal planning and health-focused tools together in one
        simple experience.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ==============================
# WELCOME
# ==============================

st.markdown(
    """
    <h3 style="
        text-align:center;
        font-size:27px;
        color:#111111;
    ">
        Welcome to ELORA
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align:center;
        max-width:700px;
        margin:15px auto;
        font-size:16px;
        line-height:1.8;
        color:#555555;
    ">
        Your everyday companion for making informed food and
        nutrition choices — designed to make healthy living
        simpler, clearer and more personal.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# ==============================
# GET STARTED
# ==============================

left, center, right = st.columns([1, 1, 1])

with center:

    if st.button(
        "Get Started",
        key="home_get_started",
        use_container_width=True
    ):
        st.switch_page("pages/1_Login.py")

# ==============================
# FOOTER
# ==============================

st.write("")
st.write("")

st.markdown(
    """
    <p style="
        text-align:center;
        font-size:13px;
        color:#777777;
        margin-top:20px;
    ">
        ELORA · Personalized Health & Nutrition
    </p>
    """,
    unsafe_allow_html=True
)