import streamlit as st


def apply_elora_theme():

    st.markdown(
        """
        <style>

        /* =========================
           ELORA BLACK & WHITE THEME
           ========================= */

        .stApp {
            background-color: #F7F7F7;
            color: #111111;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2.5rem;
            padding-bottom: 3rem;
        }

        /* =========================
           HEADINGS
           ========================= */

        h1, h2, h3, h4, h5, h6 {
            color: #111111 !important;
        }

        p, label {
            color: #222222;
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

        [data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        /* =========================
           SIDEBAR NAVIGATION
           ========================= */

        [data-testid="stSidebarNav"] {
            background-color: #111111 !important;
        }

        [data-testid="stSidebarNav"] * {
            color: #FFFFFF !important;
        }

        [data-testid="stSidebarNav"] a {
            background-color: #111111 !important;
            color: #FFFFFF !important;
        }

        [data-testid="stSidebarNav"] a:hover {
            background-color: #222222 !important;
            color: #FFFFFF !important;
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background-color: #222222 !important;
            color: #FFFFFF !important;
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] span {
            color: #FFFFFF !important;
        }

        /* =========================
           ALL BUTTONS
           ========================= */

        .stButton > button {
            background-color: #111111 !important;
            color: #FFFFFF !important;
            border: 1px solid #111111 !important;
            border-radius: 10px;
            padding: 0.55rem 1.2rem;
            font-weight: 500;
            transition: 0.2s ease;
        }

        .stButton > button p {
            color: #FFFFFF !important;
        }

        .stButton > button:hover {
            background-color: #FFFFFF !important;
            color: #111111 !important;
            border: 1px solid #111111 !important;
        }

        .stButton > button:hover p {
            color: #111111 !important;
        }

        /* =========================
           TEXT INPUTS
           ========================= */

        .stTextInput input,
        .stTextArea textarea,
        .stNumberInput input {
            background-color: #FFFFFF;
            color: #111111 !important;
            border: 1px solid #D5D5D5;
            border-radius: 8px;
        }

        /* =========================
           SELECT BOXES
           ========================= */

        .stSelectbox div[data-baseweb="select"] > div {
            background-color: #FFFFFF;
            color: #111111 !important;
            border: 1px solid #D5D5D5;
            border-radius: 8px;
        }

        [data-baseweb="select"] * {
            color: #111111 !important;
        }

        /* =========================
           NUMBER INPUT BUTTONS
           ========================= */

        .stNumberInput button {
            background-color: #FFFFFF !important;
            color: #111111 !important;
            border-color: #D5D5D5 !important;
        }

        /* =========================
           CARDS / CONTAINERS
           ========================= */

        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF;
            border: 1px solid #E2E2E2;
            border-radius: 12px;
        }

        /* =========================
           DIVIDERS
           ========================= */

        hr {
            border-color: #E0E0E0;
        }

        /* =========================
           ALERTS
           ========================= */

        [data-testid="stAlert"] {
            border-radius: 8px;
        }

        /* =========================
           LINKS
           ========================= */

        a {
            color: #111111;
        }

        </style>
        """,
        unsafe_allow_html=True
    )