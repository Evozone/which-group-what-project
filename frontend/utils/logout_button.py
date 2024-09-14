import streamlit as st


def logout_button():
    if st.button("Logout"):
        st.info("Logging out...")
        st.session_state.clear()
        st.rerun()
