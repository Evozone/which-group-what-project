import streamlit as st
from frontend.utils.sidebar import set_sidebar

set_sidebar(
    user={
        "full_name": "John Doe",
        "avatar_url": "https://avatars.githubusercontent.com/u/832385?s=200&v=4",
    }
)

st.title("My Dashboard")

# Pending requests
st.subheader("Pending Requests")

st.write("You currently have no pending requests.")
