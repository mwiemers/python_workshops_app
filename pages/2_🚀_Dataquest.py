import streamlit as st
import requests
from PIL import Image
from io import BytesIO


@st.cache
def load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image


st.set_page_config(
    page_title='Learning Python with Dataquest',
    page_icon="🚀"
)


st.markdown("""
    ## Learning Python with Dataquest

    ### Accessing Dataquest
    To start the online learning on Dataquest, please follow the below steps:

    1. [Open the survey](https://lse.eu.qualtrics.com/jfe/form/SV_e9k3I33EGgxe2xg) to request a Dataquest account. 
       We aim to provide you with access within 1-2 working days.
    2. Once you have received an email from Dataquest to inform you that you have been granted with access:
        - Read Dataquest's privacy policy before creating an account.
        - Please go to the Dataquest website and register your account with **your LSE email address**. **Do not** use your LSE email address and LSE password in combination.


    By accessing this course we ask you to note the following:
    - you are signing up for an external service 
    - you are entering an agreement with an external provider (not LSE) 
    - it is your personal account for which you are solely responsible 
    - any information uploaded may be accessible on the public web 
    - there are risks associated with entering personal data or infringing copyright law 
    
    ### The Dataquest UI

    1. The **dashboard** is accessible through the navigation bar on top of the website. Here you have access to your learning path, 
        the practice problems and the projects hub. All of these are also accessible through the navigation menu itself.

    2. The **learning path** can be changed under 'Change My Path'. For most learners the Data Scientist in Python path covers the 
        fundamentals of programming in Python, data wranling (importing, inspecting, transforming and cleaning data), data visualization and 
        machine learning. If you are not sure where to start, ask a Python trainer to help you choose a career or skill path that best suits
        your learning goals. An overview of all available courses and learning paths, is available in the [Dataquest course catalogue](https://www.dataquest.io/data-science-courses/).
        The first chapter from the Introduction to Python course also explains the UI and how to write Python code for 
        the exercises.

    3. Once you have completed a specific chapter or course, you can further deepen your understanding, consolidate your 
        learning of the syntax and practice the application of what you have learned so far with the **practice exercises**. Practice exercises are 
        available for most of the chapters from the Introduction to Python, Data visualization and Data Wrangling courses.

    4. **Guided projects** offer the opportunity to put into practice your learning by working through a project. Projects are structured 
        as a series of more challenging exercises that require you to combine your acquired skills and knowledge in more creative ways. Many of 
        the courses in your learning path will alraedy contain guided projects. Have a look at this section to find additional projects to challenge yourself.

""")

image_url = 'https://www.dropbox.com/s/msustvw138gq1o5/dq_ui.png?raw=1'
image = load_image(image_url)

st.image(image, caption='Dataquest UI')