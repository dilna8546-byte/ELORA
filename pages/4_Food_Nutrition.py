import streamlit as st
import pandas as pd
from elora_theme import apply_elora_theme

# -----------------------------
# ELORA FOOD NUTRITION THEME
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

    .stButton > button {
        background-color: #171512 !important;
        color: #FFFFFF !important;
        border: 1px solid #171512 !important;
        border-radius: 8px;
        font-weight: 600;
    }

    .stButton > button p,
    .stButton > button span {
        color: #FFFFFF !important;
    }

    .stTextInput input,
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
    page_title="ELORA - Food Nutrition",
    page_icon="🍎",
    layout="wide"
)

apply_elora_theme()

# -----------------------------
# LOAD FOOD DATA
# -----------------------------

fruits = pd.read_excel(
    "fruits and vegetables.xlsx",
    sheet_name="Sheet1"
)

vegetables = pd.read_excel(
    "fruits and vegetables.xlsx",
    sheet_name="Sheet2"
)

nuts_seeds = pd.read_excel("nuts & seeds.xlsx")
leafy_herbs = pd.read_excel("leafy greens & edible herbs.xlsx")
mushrooms = pd.read_excel("mushrooms.xlsx")
snacks_sweets = pd.read_excel("snacks & sweets.xlsx")
beverages = pd.read_excel("beverages.xlsx")
herbs_spices = pd.read_excel("herbs & spices.xlsx")
cereals_grains = pd.read_excel("cereals & grains.xlsx")
pulses_legumes = pd.read_excel("pulses & legumes.xlsx")
dairy = pd.read_excel("Dairy Products.xlsx")
fish_seafood = pd.read_excel("Fish & Seafood.xlsx")
meat_poultry_eggs = pd.read_excel("Meat, Poultry & Eggs.xlsx")

# Remove empty rows
fruits = fruits.dropna(how="all")
vegetables = vegetables.dropna(how="all")
nuts_seeds = nuts_seeds.dropna(how="all")
leafy_herbs = leafy_herbs.dropna(how="all")
mushrooms = mushrooms.dropna(how="all")
snacks_sweets = snacks_sweets.dropna(how="all")
beverages = beverages.dropna(how="all")
herbs_spices = herbs_spices.dropna(how="all")
cereals_grains = cereals_grains.dropna(how="all")
pulses_legumes = pulses_legumes.dropna(how="all")
dairy = dairy.dropna(how="all")
fish_seafood = fish_seafood.dropna(how="all")
meat_poultry_eggs = meat_poultry_eggs.dropna(how="all")

# -----------------------------
# FOOD NUTRITION ANALYZER
# -----------------------------

st.title("Food Nutrition Analyzer")

st.write(
    "Search different foods and explore their "
    "nutritional information and health benefits."
)

st.divider()

food_type = st.selectbox(
    "Choose food category:",
    [
        "🍎 Fruits",
        "🥕 Vegetables",
        "🌰 Nuts",
        "🌱 Seeds",
        "🥬 Leafy Greens & Edible Herbs",
        "🍄 Mushrooms",
        "🍿 Snacks",
        "🍰 Sweets & Desserts",
        "🥤 Beverages",
        "🌿 Herbs & Spices",
        "🍚 Cereals & Grains",
        "🫘 Pulses & Legumes",
        "🥛 Dairy Products",
        "🐟 Fish & Seafood",
        "🍗 Meat, Poultry & Eggs"
    ]
)

# -----------------------------
# SELECT DATASET
# -----------------------------

datasets = {
    "🍎 Fruits": (fruits, "Fruit Name"),
    "🥕 Vegetables": (vegetables, "Vegetable Name"),
    "🌰 Nuts": (nuts_seeds, "Food Name"),
    "🌱 Seeds": (nuts_seeds, "Food Name"),
    "🥬 Leafy Greens & Edible Herbs": (leafy_herbs, "Food Name"),
    "🍄 Mushrooms": (mushrooms, "Food Name"),
    "🍿 Snacks": (snacks_sweets, "Food Name"),
    "🍰 Sweets & Desserts": (snacks_sweets, "Food Name"),
    "🥤 Beverages": (beverages, "Food Name"),
    "🌿 Herbs & Spices": (herbs_spices, "Food Name"),
    "🍚 Cereals & Grains": (cereals_grains, "Food Name"),
    "🫘 Pulses & Legumes": (pulses_legumes, "Food Name"),
    "🥛 Dairy Products": (dairy, "Food Name"),
    "🐟 Fish & Seafood": (fish_seafood, "Food Name"),
    "🍗 Meat, Poultry & Eggs": (meat_poultry_eggs, "Food Name")
}

data, name_column = datasets[food_type]

# -----------------------------
# SELECT FOOD
# -----------------------------

food_list = (
    data[name_column]
    .dropna()
    .astype(str)
    .str.strip()
    .drop_duplicates()
    .tolist()
)

selected_food = st.selectbox(
    "Choose a food:",
    ["Select a food"] + food_list
)

if selected_food != "Select a food":

    food = data[
        data[name_column].astype(str).str.strip()
        == selected_food.strip()
    ].iloc[0]

    st.divider()

    st.subheader(selected_food)

    # Nutrition values
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if "Calories/100g" in data.columns:
            st.metric(
                "Calories",
                f"{food['Calories/100g']} kcal"
            )

    with col2:
        if "Carbs (g)" in data.columns:
            st.metric(
                "Carbs",
                f"{food['Carbs (g)']} g"
            )

    with col3:
        if "Protein (g)" in data.columns:
            st.metric(
                "Protein",
                f"{food['Protein (g)']} g"
            )

    with col4:
        if "Fat (g)" in data.columns:
            st.metric(
                "Fat",
                f"{food['Fat (g)']} g"
            )

    with col5:
        if "Fiber (g)" in data.columns:
            st.metric(
                "Fiber",
                f"{food['Fiber (g)']} g"
            )

    st.divider()

    if "Category" in data.columns:
        st.write(f"**Category:** {food['Category']}")

    if "Main Nutrients" in data.columns:
        st.write(
            f"**Main Nutrients:** {food['Main Nutrients']}"
        )

    if "Health Benefits" in data.columns:
        st.write(
            f"**Health Benefits:** {food['Health Benefits']}"
        )

    if "Diabetes Suitability" in data.columns:
        st.write(
            f"**Diabetes Suitability:** "
            f"{food['Diabetes Suitability']}"
        )

    if "Heart Health Rating" in data.columns:
        st.write(
            f"**Heart Health Rating:** "
            f"{food['Heart Health Rating']}"
        )

    if "Weight Management" in data.columns:
        st.write(
            f"**Weight Management:** "
            f"{food['Weight Management']}"
        )

    if "Baby Suitable Age" in data.columns:
        st.write(
            f"**Baby Suitable Age:** "
            f"{food['Baby Suitable Age']}"
        )

    if "Allergy Notes" in data.columns:
        st.write(
            f"**Allergy Notes:** "
            f"{food['Allergy Notes']}"
        )

    if "Portion Recommendation" in data.columns:
        st.write(
            f"**Portion Recommendation:** "
            f"{food['Portion Recommendation']}"
        )

    if "Source" in data.columns:
        st.write(
            f"**Source:** {food['Source']}"
        )