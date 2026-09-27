import os
import base64
import streamlit as st
from google import genai
from google.genai import types

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="ELORA | Food Photo Analyzer",
    page_icon="🍽️",
    layout="wide"
)

# --------------------------------------------------
# ELORA BLACK & WHITE THEME
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #F7F7F7;
        color: #111111;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #111111 !important;
    }

    p, label {
        color: #222222;
    }

    [data-testid="stSidebar"] {
        background-color: #111111;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    .stButton > button {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 1px solid #111111 !important;
        border-radius: 10px;
        padding: 0.55rem 1.2rem;
        font-weight: 500;
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

    .result-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E2E2;
        border-radius: 14px;
        padding: 24px;
        margin-top: 15px;
    }

    hr {
        border-color: #E0E0E0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# GEMINI API
# --------------------------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key was not found.")
    st.info(
        'In PowerShell, run: $env:GEMINI_API_KEY="YOUR_API_KEY"'
    )
    st.stop()

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=60000
    )
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.caption("ELORA")

st.title("FOOD PHOTO ANALYZER")

st.write(
    "Upload or take a photo of food and let AI identify it "
    "and provide an estimated nutritional analysis."
)

st.divider()

# --------------------------------------------------
# IMAGE INPUT
# --------------------------------------------------

st.subheader("UPLOAD OR TAKE A FOOD PHOTO")

uploaded_file = st.file_uploader(
    "Choose a food image",
    type=["jpg", "jpeg", "png", "webp"]
)

camera_file = st.camera_input(
    "Or take a photo"
)

image_file = (
    uploaded_file
    if uploaded_file is not None
    else camera_file
)

# --------------------------------------------------
# IMAGE PREVIEW
# --------------------------------------------------

if image_file is not None:

    st.image(
        image_file,
        caption="Selected food image",
        width=500
    )

    st.write("")

    # --------------------------------------------------
    # ANALYZE BUTTON
    # --------------------------------------------------

    if st.button(
        "ANALYZE FOOD",
        use_container_width=True
    ):

        image_bytes = image_file.getvalue()

        image_base64 = base64.b64encode(
            image_bytes
        ).decode("utf-8")

        mime_type = (
            image_file.type
            or "image/jpeg"
        )

        # --------------------------------------------------
        # AI PROMPT
        # --------------------------------------------------

        prompt = """
You are ELORA, an AI-powered food and nutrition assistant.

Analyze the food shown in this image.

Give the response using exactly these sections:

FOOD NAME:
The most likely name of the food.

DESCRIPTION:
A short description of what is shown.

ESTIMATED NUTRITION:
Calories:
Carbohydrates:
Protein:
Fat:
Fiber:
Sodium:

MAIN NUTRIENTS:
Important vitamins, minerals, or other nutrients.

HEALTH INFORMATION:
A short general explanation of the nutritional characteristics.

PORTION NOTE:
Give a general portion reference if possible.

IMPORTANT:
Nutrition values estimated from an image are approximate.
The exact ingredients, portion size, preparation method,
and nutritional values cannot be determined from an image alone.

Do not diagnose diseases.
Do not provide medication advice.
"""

        # --------------------------------------------------
        # AI ANALYSIS
        # --------------------------------------------------

        try:

            with st.spinner(
                "AI is analyzing your food image..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=[
                        types.Part.from_text(
                            text=prompt
                        ),
                        types.Part.from_bytes(
                            data=image_bytes,
                            mime_type=mime_type
                        )
                    ]
                )

            result = response.text

            # --------------------------------------------------
            # RESULT
            # --------------------------------------------------

            st.divider()

            st.subheader("AI FOOD ANALYSIS")

            st.markdown(
                f"""
                <div class="result-card">
                    {result.replace(chr(10), "<br>")}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            st.warning(
                "Nutrition values shown here are AI-based estimates. "
                "Actual nutrition can vary depending on ingredients, "
                "portion size, preparation, and serving method."
            )

        except Exception as e:

            st.error(
                "The AI analysis could not be completed."
            )

            st.warning(
                "Please try again."
            )

            st.caption(
                str(e)
            )