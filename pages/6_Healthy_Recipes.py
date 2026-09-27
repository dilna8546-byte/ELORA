import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ELORA - Healthy Recipes",
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
       HEADINGS
       ========================= */

    h1, h2, h3, h4, h5, h6 {
        color: #111111 !important;
    }

    p,
    label,
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

    /* SIDEBAR PAGE NAMES */

    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebarNav"] a span,
    [data-testid="stSidebarNav"] a p,
    [data-testid="stSidebarNav"] li,
    [data-testid="stSidebarNav"] li span,
    [data-testid="stSidebarNav"] li p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        background-color: #111111 !important;
    }

    /* SIDEBAR HOVER */

    [data-testid="stSidebarNav"] a:hover,
    [data-testid="stSidebarNav"] a:hover span,
    [data-testid="stSidebarNav"] a:hover p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        background-color: #222222 !important;
    }

    /* SELECTED PAGE */

    [data-testid="stSidebarNav"] a[aria-current="page"],
    [data-testid="stSidebarNav"] a[aria-current="page"] span,
    [data-testid="stSidebarNav"] a[aria-current="page"] p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        background-color: #222222 !important;
    }

    /* =========================
       BUTTONS
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
       SELECT BOX
       ========================= */

    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5 !important;
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
# LOAD RECIPE DATA
# -----------------------------

recipes = pd.read_excel(
    "Breakfast Recipes.xlsx"
)

recipes = recipes.dropna(how="all")

# -----------------------------
# HEALTHY RECIPE GENERATOR
# -----------------------------

st.title("Healthy Recipe Generator")

st.write(
    "Find healthy recipes based on your dietary needs."
)

st.divider()

recipe_category = st.selectbox(
    "Choose a recipe category:",
    ["All"] + sorted(
        recipes["Category"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
        .tolist()
    ),
    key="recipe_category_page"
)

recipe_condition = st.selectbox(
    "Choose a health preference:",
    [
        "All",
        "Diabetes Suitable",
        "Heart Healthy",
        "Weight Loss",
        "Baby Suitable"
    ],
    key="recipe_condition_page"
)

if st.button(
    "Find Recipes",
    key="find_recipes_page"
):

    filtered_recipes = recipes.copy()

    if recipe_category != "All":
        filtered_recipes = filtered_recipes[
            filtered_recipes["Category"]
            .astype(str)
            .str.strip()
            == recipe_category
        ]

    if recipe_condition == "Baby Suitable":
        filtered_recipes = filtered_recipes[
            filtered_recipes["Baby Suitable"]
            .astype(str)
            .str.strip()
            .str.lower()
            != "not for infants"
        ]

    elif recipe_condition != "All":
        filtered_recipes = filtered_recipes[
            filtered_recipes[recipe_condition]
            .astype(str)
            .str.strip()
            .str.lower()
            == "yes"
        ]

    if not filtered_recipes.empty:

        st.success(
            f"Found {len(filtered_recipes)} matching recipes."
        )

        for _, recipe in filtered_recipes.head(10).iterrows():

            st.subheader(recipe["Recipe Name"])

            st.write(
                f"**Cuisine:** {recipe['Cuisine']}"
            )

            st.write(
                f"**Ingredients:** {recipe['Ingredients']}"
            )

            st.write(
                f"**Instructions:** {recipe['Instructions']}"
            )

            st.write(
                f"*Calories:* {recipe['Calories']}"
            )

            st.write(
                f"*Carbs:* {recipe['Carbs (g)']} g"
            )

            st.write(
                f"*Protein:* {recipe['Protein (g)']} g"
            )

            st.write(
                f"*Fat:* {recipe['Fat (g)']} g"
            )

            st.write(
                f"*Fiber:* {recipe['Fiber (g)']} g"
            )

            st.write(
                f"*Prep:* {recipe['Prep Time']} | "
                f"**Cook:** {recipe['Cook Time']}"
            )

            st.write(
                f"*Allergens:* {recipe['Allergens']}"
            )

            st.write(
                f"*Source:* {recipe['Source']}"
            )

            st.divider()

    else:
        st.warning(
            "No recipes matched your selected preferences."
        )