import streamlit as st

from theme import apply_elora_theme

st.set_page_config(
    page_title="ELORA - Track Recovery",
    page_icon="🌿",
    layout="wide"
)

apply_elora_theme()

st.title("Track Recovery")
st.write("Record your daily wellness progress and keep track of how you are feeling.")

st.divider()

# DAILY WELLNESS STATUS

st.subheader("Daily Wellness")

recovery_status = st.selectbox(
    "How are you feeling today?",
    [
        "Select status",
        "Feeling better",
        "Feeling the same",
        "Feeling a little unwell",
        "Would like to talk to a healthcare professional"
    ]
)

recovery_notes = st.text_area(
    "Add a short note about your day",
    placeholder="Example: Followed my meal plan and drank enough water."
)

st.divider()

# SAVE UPDATE

if st.button("Save Recovery Update"):

    if recovery_status == "Select status":
        st.warning("Please select how you are feeling today.")

    else:
        st.session_state["recovery_update"] = {
            "Status": recovery_status,
            "Notes": recovery_notes
        }

        st.success("Recovery update saved successfully!")

# DISPLAY LATEST UPDATE

if "recovery_update" in st.session_state:

    st.divider()

    st.subheader("Latest Recovery Update")

    update = st.session_state["recovery_update"]

    st.write(f"**Status:** {update['Status']}")

    if update["Notes"]:
        st.write(f"**Notes:** {update['Notes']}")
    else:
        st.write("**Notes:** No notes added.")

st.divider()

st.caption(
    "This tracker is for personal wellness tracking and does not diagnose "
    "or monitor medical conditions."
)