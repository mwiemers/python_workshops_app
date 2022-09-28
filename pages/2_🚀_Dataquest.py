import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title='Learning Python with Dataquest',
    page_icon="🚀"
)


st.markdown("""
    ## Learning Python with Dataquest

    ### Accessing Dataquest
    1. Request a coupon to set up your Dataquest licence via [this survey](https://qualtrics.com). The DSL will email you the 
        coupon within 1-2 days. The first courses on Dataquest from the Introduction to Python skill path are free, but 
        ensure to request your licence to be able to continue to learn the following courses.

    2. Once you have your received your coupon. Set up your account on [dataquest.io](https://app.dataquest.io/signup) 
        using your **LSE email address**. **Do not** use your LSE email address and LSE password in combination.        
    
    ### The Dataquest UI

    1. The **dashboard** is accessible through the navigation bar on top of the website. Here you have access to your learning path, 
        the practice problems and the projects hub. All of these are also accessible through the navigation menu itself.

    2. The **learning path** can be changed under 'Change My Path'. For most learners the Data Scientist in Python path covers the 
        fundamentals of programming in Python, data wranling (importing, inspecting, transforming and cleaning data), data visualization and 
        machine learning. If you are not sure where to start, ask a Python trainer to help you choose a career or skill path that best suits
        your learning goals. The first chapter from the Introduction to Python course also explains the UI and how to write Python code for 
        the exercises.

    
    3. Once you have completed a specific chapter or course, you can further deepen your understanding, consolidate your 
        learning of the syntax and practice the application of what you have learned so far with the **practice exercises**. Practice exercises are 
        available for most of the chapters from the Introduction to Python, Data visualization and Data Wrangling courses.

    4. **Guided projects** offer the opportunity to put into practice your learning by working through a project. Projects are structured 
        as a series of more challenging exercises that require you to combine your acquired skills and knowledge in more creative ways. Many of 
        the courses in your learning path will alraedy contain guided projects. Have a look at this section to find additional projects to challenge yourself.

""")

response = requests.get('https://www.dropbox.com/s/msustvw138gq1o5/dq_ui.png?raw=1')
image = Image.open(BytesIO(response.content))

st.image(image, caption='Dataquest UI')