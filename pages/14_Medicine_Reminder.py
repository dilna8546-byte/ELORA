import streamlit as st
from datetime import time

st.set_page_config(
    page_title="ELORA - Medicine Reminder",
    page_icon="",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        background-color: #F7F7F7 !important;
        color: #111111 !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #111111 !important;
    }

    p,
    label,
    span,
    .stMarkdown {
        color: #222222 !important;
    }

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

    [data-testid="stSidebarNav"] a span,
    [data-testid="stSidebarNav"] a div,
    [data-testid="stSidebarNav"] a p {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

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

    .stTextInput input,
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5 !important;
        border-radius: 8px !important;
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: #777777 !important;
    }

    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5 !important;
        border-radius: 8px !important;
    }

    [data-testid="stSelectbox"] div[data-baseweb="select"] * {
        color: #111111 !important;
    }

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

    [data-testid="stTimeInput"] input {
        background-color: #FFFFFF !important;
        color: #111111 !important;
        border: 1px solid #D5D5D5 !important;
        border-radius: 8px !important;
    }

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

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E2E2 !important;
        border-radius: 12px !important;
    }

    hr {
        border-color: #E0E0E0 !important;
    }

    [data-testid="stAlert"] {
        border-radius: 8px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "medicine_reminders" not in st.session_state:
    st.session_state.medicine_reminders = []

st.title("Medicine Reminder")

st.write(
    "Keep track of your medicine reminders in one simple place."
)

st.divider()

st.subheader("Add a Medicine Reminder")

col1, col2 = st.columns(2)

with col1:
    medicine_name = st.text_input(
        "Medicine Name",
        placeholder="Enter medicine name"
    )

with col2:
    reminder_time = st.time_input(
        "Reminder Time",
        value=time(8, 0)
    )

frequency = st.selectbox(
    "Frequency",
    [
        "Once a day",
        "Twice a day",
        "Three times a day",
        "As needed"
    ]
)

note = st.text_area(
    "Optional Note",
    placeholder="Add a note if needed..."
)

if st.button("Add Reminder", key="add_medicine_reminder"):

    if medicine_name.strip():

        reminder = {
            "medicine": medicine_name.strip(),
            "time": reminder_time.strftime("%I:%M %p"),
            "frequency": frequency,
            "note": note.strip()
        }

        st.session_state.medicine_reminders.append(reminder)

        st.success("Medicine reminder added successfully.")

    else:
        st.warning("Please enter a medicine name.")

st.divider()

st.subheader("Your Reminders")

if len(st.session_state.medicine_reminders) == 0:

    st.info("No medicine reminders have been added yet.")

else:

    for index, reminder in enumerate(
        st.session_state.medicine_reminders
    ):

        with st.container(border=True):

            st.markdown(
                f"### {reminder['medicine']}"
            )

            st.write(
                f"**Time:** {reminder['time']}"
            )

            st.write(
                f"**Frequency:** {reminder['frequency']}"
            )

            if reminder["note"]:
                st.write(
                    f"**Note:** {reminder['note']}"
                )

            if st.button(
                "Delete Reminder",
                key=f"delete_reminder_{index}"
            ):

                st.session_state.medicine_reminders.pop(index)

                st.rerun()

st.divider()

st.info(
    "This feature is only a reminder tool. It does not provide "
    "medical advice, prescribe medicines, or recommend dosages. "
    "Follow the instructions given by your healthcare professional."
)