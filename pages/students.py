from backend.students import get_students
from frontend.utils.sidebar import set_sidebar
import streamlit as st

set_sidebar()
st.title("Students in PCE Comp Engg")


def show_students():
    students = get_students()
    st.dataframe(students, width=1000, height=500)


def main():
    show_students()


main()
