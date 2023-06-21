import streamlit as st


st.set_page_config(
    page_title='Python Workshop Format',
    page_icon='👨‍🏫'
)

st.title("The Python Workshop Format")

st.markdown("""

    ## DSL Python workshops

    Our Python workshops are split into two type of sessions:
    1) Python Introduction
    2) Python for Data Science

    Both of these workshops are open-format, which means that you can choose which topic to work on. It is advised to work through the materials 
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
    - Final Coding Challenges

    ### Python Data Wrangling and Visualisation
    Once you have completed the materials from the Python Introduction series or in case you are already familiar with these topics, feel free 
    to move on to the Python Data Wrangling and Visualisation series where you will learn about more complex fundamental programming concepts and how to 
    use libraries to manipulate and visualize data in Python.

    The Python Data Wrangling and Visualisation workshops cover the following topics:  
      
    Python Data Wrangling
    - NumPy arrays
    - NumPy 2D arrays
    - Pandas Basics
    - Pandas Indexing
    - Pandas Exploring Data

    Python Data Visualization
    - Line plots with matplotlib
    - Scatter, Bar, Histogram with Matplotlib
    - Seaborn and Pandas plots



    ### What to do when you get stuck:


    If you get stuck, we recommend to:

    - Ask one of our Python experts for help
    - Ask ChatGPT for help with the tasks
    - Search online (here are a couple of useful resources):
        - The answer box on the top of Google's results page
        - [Stackoverflow](https://stackoverflow.com) (for task specific solutions)
        - [RealPython](https://realpython.com) (for topic based tutorials)
        - [w3schools](https://w3schools.com]) (for short task specific tutorials and examples)
    - Ask your fellow students
    
    """
)