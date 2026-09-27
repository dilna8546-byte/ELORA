import streamlit as st
from elora_theme import apply_elora_theme

st.set_page_config(
    page_title="ELORA - Login",
    page_icon="",
    layout="centered"
)

apply_elora_theme()

# -----------------------------
# ELORA LOGIN THEME
# -----------------------------

st.markdown(
    """
    <style>

    /* =========================
       LOGIN PAGE
       ========================= */

    .stApp {
        background-color: #F7F7F7;
        color: #111111;
    }

    h1, h2, h3 {
        color: #111111 !important;
        text-align: center;
    }

    p, label {
        color: #222222 !important;
    }

    /* =========================
       LOGIN BOX
       ========================= */

    .login-box {
        background-color: #FFFFFF;
        padding: 35px;
        border-radius: 16px;
        border: 1px solid #E0E0E0;
        margin-top: 40px;
    }

    /* =========================
       TEXT INPUTS
       ========================= */

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5;
        border-radius: 8px;
    }

    /* =========================
       LOGIN BUTTON
       ========================= */

    .stButton > button {
        width: 100%;
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #111111 !important;
        border-radius: 8px;
        padding: 0.6rem;
        font-weight: 600;
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

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# LOGIN
# -----------------------------

st.markdown(
    """
    <div class="login-box">
        <h1>ELORA</h1>
        <p style="text-align:center;">
            Health & Nutrition Assistant
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username and password:
        st.success("Login successful!")
        st.switch_page("pages/2_Dashboard.py")

    else:
        st.warning(
            "Please enter your username and password."
        )
