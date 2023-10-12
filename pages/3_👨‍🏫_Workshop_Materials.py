import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Python Workshop Format',
    page_icon='👨‍🏫'
)

local_css("css/style.css")

st.title("The Python Workshop Format")

st.markdown("""

    ## DSL Python workshops

    The Python Fundamentals workshops are open-format, which means that you can choose which topic to work on. It is advised to work through the materials 
    in order unless you are already familiar with a particular topic.

    Each workshop is **two-hours** long, and you will work **with fellow learners**, utilising your **prior experience**, **web searches**, 
    and in-application Help features to find the solutions to real-world problems, with a **Python expert** on hand if you get stuck.

    ### Python Fundamentals
    The Python Introduction workshops are for beginners that have no prior experience in programming with Python and cover the following topics:
    Python Fundamentals:
    - Numerical variables
    - String variables
    - Type casting
    - Lists
    - For loops
    - Conditionals
    - Writing functions
    - Dictionaries
    - While Loops
    - Final Coding Challenges
        
    """)
with open("materials/PF_notebooks.zip", "rb") as f:
    btn = st.download_button(
        label = "Download Python Fundamentals materials",
        data = f,
        file_name = "PF_notebooks.zip",
        mime = "application/zip"
        )

st.markdown("""

    ### Python Data Wrangling and Visualisation
    Once you have completed the materials from the Python Introduction series or in case you are already familiar with these topics, feel free 
    to move on to the Python Data Wrangling and Visualisation materials where you how to use specific libraries to manipulate and visualize data in Python.
 
    Python Data Wrangling
    - NumPy arrays
    - NumPy 2D arrays
    - Pandas Basics
    - Pandas Indexing
    - Pandas Exploring Data

""")

with open("materials/PDW_notebooks.zip", "rb") as f:
    st.download_button(
        label="Download Python Data Wrangling materials as zip file",
        data=f,
        file_name='PDW_notebooks.zip',
        mime='application/x-zip',
    )

st.markdown("""
    Python Data Visualization
    - Line plots with matplotlib
    - Scatter, Bar, Histogram with Matplotlib
    - Seaborn and Pandas plots
""")

with open("materials/PDV_notebooks.zip", "rb") as f:
    st.download_button(
        label="Download Python Data Visualisation materials as zip file",
        data=f,
        file_name='PDV_notebooks.zip',
        mime='application/x-zip',
    )

st.markdown("""


    ### What to do when you get stuck:


    If you get stuck, we recommend to:

    - Ask one of our Python experts for help
    - Search online (here are a couple of useful resources):
        - The answer box on the top of Google's results page
        - [Stackoverflow](https://stackoverflow.com) (for task specific solutions)
        - [RealPython](https://realpython.com) (for topic based tutorials)
        - [w3schools](https://w3schools.com]) (for short task specific tutorials and examples)
    - Ask your fellow students
    
    """
)