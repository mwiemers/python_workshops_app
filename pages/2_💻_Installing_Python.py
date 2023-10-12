import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from load_css import local_css


@st.cache_resource
def load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image


st.set_page_config(
    page_title='Installing Python',
    page_icon="💻"
)

local_css("css/style.css")

st.markdown("""
## Chosing an installation
        
There are several ways to work with Python on your laptop. To get started we will stick to the simplest option, Anaconda Navigator. 
        
Anaconda Navigator consists of the following:
* The latest version of **Python**
* A large collection of **libraries** for data science
* A package and environment manager called **conda**
* A graphical user interface called Anaconda Navigator
""")

st.image("img/anaconda_graphic.png", caption='Anaconda')


st.markdown(
    """
### Installing Anaconda Navigator
    
Installing Python using Anaconda Navigator is a simple process. 
        
#### Mac:
1. Depending on whether your Mac has an M1/M2 or Intel processor, you will have to download a different version of Anaconda. Check the processor 
        type by clicking on the Apple icon in the top left corner of your screen and selecting About this Mac. 
        If you have an M1/M2 processor, you will see Apple M1 in the Overview tab. If you have an Intel processor, you will see Intel in the Overview tab.
""")
st.image("img/mac_processor.png")

st.markdown(
    """
2. Download the installer for your specific processor from [anaconda.com](https://www.anaconda.com/products/individual).
""")

st.image("img/install_anaconda_01.png")

st.markdown("""
3. Run the installer. Do not change any of the default settings.

#### Windows:
1. Download the installer for your operating system from [anaconda.com](https://www.anaconda.com/products/individual).
2. Run the installer. Do not change any of the default settings.
"""
            )



