import streamlit as st


st.set_page_config(
    page_title='Python Workshop Format',
    page_icon='👨‍🏫'
)

st.title("The Python Workshop Format")

st.markdown("""

    # DSL Python workshops

    Our Python workshops are split into two type of sessions:
    1) Python Introduction
    2) Python for Data Science

    Both of these workshops are open-format, which means that you can choose which topic to work on. It is advised to work through the materials 
    in order unless you are already familiar with a particular topic.

    Each workshop is **two-hours** long, and you will work **with fellow learners**, utilising your **prior experience**, **web searches**, 
    and in-application Help features to find the solutions to real-world problems, with a **Python expert** on hand if you get stuck.

    ## Python Introduction
    The Python Introduction workshops are for beginners that have no prior experience in programming with Python and cover the following topics:
    Python Fundamentals:
    - Numerical variables
    - String variables
    - Type casting
    - Lists

    ## Python for Data Science
    Once you have completed the materials from the Python Introduction series or in case you are already familiar with these topics, feel free 
    to move on to the Python for Data Science series where you will learn about more complex fundamental programming concepts and how to 
    use libraries to manipulate and visualize data in Python.

    The Python for Data Science workshops cover the following topics:
    Python Fundamentals:
    - List of lists
    - Functions and modules
    - For loops
    - Conditionals
    - Writing functions
    - Guided Project: Zoopla Rent Prices

    Python Data Wrangling:
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

    On Dataquest you have the option to see the solution for each exercise. We highly recommend to only use that as a last resort when you 
    have explored all other options. Being able to search effectively online, identify relevant resources and use them to fix your code 
    are very important skills to enable you to continue to learn independently.

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