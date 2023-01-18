import requests
import yfinance as yf
import streamlit as st
from io import BytesIO
from PIL import Image

@st.cache
def load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

st.set_page_config(
    page_title='Learning Python at the Digital Skills Lab',
    page_icon="🐍"
)

st.title("Learning Python at the DSL")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Developer (Data Science Tools)  
    Digital Skills Lab  

    ---

    """)


cols = st.columns(3)
image_url = 'https://www.dropbox.com/s/ixpdexahj1h5mjw/python.png?raw=1'

image = load_image(image_url)

with cols[1]:
    st.image(image, caption='Python Logo')


st.markdown(
    """
    This website provides an introduction to the Python workshops at the Digital Skills Lab.

    Please select a page from the sidebar menu where you can find information about:
    - why Python is such a popular programming language and why you should learn it
    - information on how you can install Python on your personal laptop or PC
    - the format of the Python workshops
    - how to access the Python workshop materials on Teams

    """)


