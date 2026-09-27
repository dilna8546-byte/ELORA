import os
import streamlit as st
from google import genai
from google.genai import types


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ELORA | AI Health Chatbot",
    page_icon="✦",
    layout="wide"
)


# =========================================================
# ELORA THEME
# =========================================================

st.markdown("""
<style>

    /* =====================================================
       MAIN PAGE
       ===================================================== */

    .stApp {
        background-color: #F7F7F7;
        color: #111111;
    }

    .main .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background-color: #111111 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }


    /* =====================================================
       HEADINGS
       ===================================================== */

    h1, h2, h3, h4, h5, h6 {
        color: #111111 !important;
    }


    /* =====================================================
       NEW CHAT
       ===================================================== */

    .stButton > button {
        background-color: transparent !important;
        color: #111111 !important;
        border: 1px solid #BDBDBD !important;
        border-radius: 7px !important;
        font-weight: 500 !important;
        min-height: 35px !important;
        box-shadow: none !important;
    }

    .stButton > button:hover {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border-color: #111111 !important;
    }

    .stButton > button:focus,
    .stButton > button:active {
        border-color: #111111 !important;
        box-shadow: none !important;
        outline: none !important;
    }


    /* =====================================================
       REMOVE NATIVE MESSAGE BOX
       ===================================================== */

    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0.35rem 0 !important;
        margin-bottom: 0.8rem !important;
    }


    /* =====================================================
       MESSAGE CONTENT
       ===================================================== */

    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }


    /* =====================================================
       USER MESSAGE
       ===================================================== */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {
        justify-content: flex-end !important;
    }


    /* =====================================================
       USER MESSAGE CONTENT
       ===================================================== */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) [data-testid="stChatMessageContent"] {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border-radius: 16px 16px 4px 16px !important;
        padding: 10px 15px !important;
        max-width: 70% !important;
    }


    /* =====================================================
       USER TEXT
       ===================================================== */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) [data-testid="stChatMessageContent"] p {
        color: #FFFFFF !important;
    }


    /* =====================================================
       ASSISTANT MESSAGE
       ===================================================== */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) [data-testid="stChatMessageContent"] {
        background-color: transparent !important;
        color: #111111 !important;
        padding: 8px 0 !important;
        max-width: 70% !important;
    }


    /* =====================================================
       ASSISTANT TEXT
       ===================================================== */

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) [data-testid="stChatMessageContent"] p {
        color: #111111 !important;
    }


    /* =====================================================
       AVATARS
       ===================================================== */

    [data-testid="stChatMessage"] [data-testid*="Avatar"] {
        filter: grayscale(100%) !important;
    }

    [data-testid="stChatMessage"] [data-testid*="Avatar"] svg {
        filter: grayscale(100%) brightness(0) invert(1) !important;
    }


    /* =====================================================
       CHAT INPUT
       ===================================================== */

    [data-testid="stChatInput"] {
        border: 1px solid #AFAFAF !important;
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
        outline: none !important;
        box-shadow: none !important;
    }

    [data-testid="stChatInput"]:focus-within {
        border: 1px solid #111111 !important;
        outline: none !important;
        box-shadow: none !important;
    }

    [data-testid="stChatInput"] > div {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }


    /* =====================================================
       TEXT AREA
       ===================================================== */

    [data-testid="stChatInput"] textarea {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        background-color: #FFFFFF !important;
        color: #111111 !important;
    }

    [data-testid="stChatInput"] textarea:focus {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }


    /* =====================================================
       SEND ARROW
       ===================================================== */

    [data-testid="stChatInput"] button {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        color: #111111 !important;
        border-radius: 0 !important;
    }

    [data-testid="stChatInput"] button svg {
        color: #111111 !important;
        fill: #111111 !important;
        stroke: #111111 !important;
    }

    [data-testid="stChatInput"] button:hover,
    [data-testid="stChatInput"] button:focus,
    [data-testid="stChatInput"] button:active {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }


    /* =====================================================
       REMOVE BROWN ACCENT
       ===================================================== */

    [data-testid="stChatInput"] *:focus,
    [data-testid="stChatInput"] *:focus-visible,
    [data-testid="stChatInput"] *:active {
        outline-color: transparent !important;
    }


    /* =====================================================
       INFO BOX
       ===================================================== */

    [data-testid="stAlert"] {
        border-radius: 10px !important;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {
        border-color: #DDDDDD !important;
    }


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 700px) {

        [data-testid="stChatMessage"]:has(
            [data-testid="chatAvatarIcon-user"]
        ) [data-testid="stChatMessageContent"],
        [data-testid="stChatMessage"]:has(
            [data-testid="chatAvatarIcon-assistant"]
        ) [data-testid="stChatMessageContent"] {
            max-width: 82% !important;
        }

    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# GEMINI API
# =========================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(
        "Gemini API key was not found. "
        "Please set the GEMINI_API_KEY environment variable."
    )
    st.stop()


client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=60000
    )
)


# =========================================================
# ELORA AI INSTRUCTIONS
# =========================================================

SYSTEM_INSTRUCTION = """
You are ELORA, an AI health, nutrition and wellness assistant.

You are a friendly, clear and helpful conversational AI.

You can answer:

- General questions
- Health questions
- Nutrition questions
- Food questions
- Wellness questions
- Lifestyle questions
- Everyday questions
- Educational questions
- Casual conversation

Important safety rules:

1. Provide general educational information.
2. Do not diagnose diseases.
3. Do not prescribe medicines.
4. Do not recommend changing medication or dosage.
5. Do not provide dangerous medical instructions.
6. If a situation sounds urgent or potentially dangerous, encourage
   the user to contact a qualified healthcare professional or
   appropriate emergency service.
7. Clearly mention uncertainty when information cannot be determined
   reliably.
8. Do not pretend to be a doctor.
9. Keep explanations understandable for a student.
10. Answer naturally instead of sounding like a fixed FAQ.
11. Use the conversation history to understand follow-up questions.
12. You may answer questions outside health and nutrition too.
13. Do not claim that an image, symptom or description is enough
   to make a medical diagnosis.

Your goal is to provide useful, responsible and easy-to-understand
information.
"""


# =========================================================
# CHAT MEMORY
# =========================================================

if "elora_chat_history" not in st.session_state:
    st.session_state.elora_chat_history = []


# =========================================================
# HEADER
# =========================================================

st.caption("ELORA")

st.title("AI HEALTH CHATBOT")

st.write(
    "Your AI health, nutrition and wellness companion."
)


# =========================================================
# NEW CHAT
# =========================================================

if st.session_state.elora_chat_history:

    if st.button("NEW CHAT"):
        st.session_state.elora_chat_history = []
        st.rerun()


# =========================================================
# WELCOME SCREEN
# =========================================================

if not st.session_state.elora_chat_history:

    st.divider()

    st.subheader("How can I help you today?")

    st.write(
        "Ask ELORA anything. You can talk about health, nutrition, "
        "food, wellness, lifestyle, everyday questions, or anything "
        "else you'd like to know."
    )

    st.write("")

    st.info(
        "ELORA is powered by AI and generates responses dynamically "
        "based on your questions."
    )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.elora_chat_history:

    if message["role"] == "user":

        with st.chat_message("user"):
            st.write(message["content"])

    else:

        with st.chat_message("assistant"):
            st.write(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

user_prompt = st.chat_input(
    "Ask ELORA anything..."
)


# =========================================================
# PROCESS USER MESSAGE
# =========================================================

if user_prompt:

    # -----------------------------------------------------
    # Save user message
    # -----------------------------------------------------

    st.session_state.elora_chat_history.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )


    # -----------------------------------------------------
    # Prepare conversation
    # -----------------------------------------------------

    conversation = []

    for message in st.session_state.elora_chat_history:

        conversation.append(
            types.Content(
                role=message["role"],
                parts=[
                    types.Part.from_text(
                        text=message["content"]
                    )
                ]
            )
        )


    # -----------------------------------------------------
    # Generate AI response
    # -----------------------------------------------------

    with st.spinner("ELORA is thinking..."):

        try:

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=conversation,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.7
                )
            )

            ai_response = response.text

            if not ai_response:

                ai_response = (
                    "I'm sorry, I couldn't generate a response "
                    "right now. Please try again."
                )

        except Exception as e:

            ai_response = (
                "I'm having trouble connecting to the AI service "
                "right now. Please try again in a moment."
            )

            print("Gemini error:", e)


    # -----------------------------------------------------
    # Save AI response
    # -----------------------------------------------------

    st.session_state.elora_chat_history.append(
        {
            "role": "model",
            "content": ai_response
        }
    )


    # -----------------------------------------------------
    # Refresh
    # -----------------------------------------------------

    st.rerun()


# =========================================================
# INFORMATION NOTICE
# =========================================================

st.divider()

st.caption(
    "ELORA provides general educational information generated by AI. "
    "It does not replace professional medical advice, diagnosis or treatment."
)