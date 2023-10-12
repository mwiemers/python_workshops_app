import streamlit as st
from load_css import local_css


st.set_page_config(
    page_title='Learning Python at the Digital Skills Lab',
    page_icon="🐍"
)

local_css("css/style.css")

st.title("Learning Python at the DSL")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Developer (Data Science Tools)  
    """)

st.image("img/lse_dsl_logo.png", width=400)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/python_logo.png", width=150)

st.markdown(
    """
    This website provides an introduction to the Python workshops at the Digital Skills Lab.

    Please select a page from the sidebar menu where you can find information about:
    - why Python is such a popular programming language and why you should learn it
    - how to install Python/Anaconda on your personal laptop (you can skip this if you're using a teaching PC)
    - the workshop lessons including download links
    - how to open the workshop lessons on your PC/personal laptop

    """)


