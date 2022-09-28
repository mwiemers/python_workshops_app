from gettext import npgettext
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import pandas_datareader.data as web
from PIL import Image
import requests
from io import BytesIO

def main():

    page = st.sidebar.selectbox("Choose a page", ['Why learn Python', 'Learning Python with Dataquest', 'The workshop format'])
    
    
    if page == 'Why learn Python':
        st.title("Learning Python at the Digital Skills Lab")
        st.markdown(
            """
            **Michael Wiemers**  
            Learning Developer (Data Science Tools)  
            Digital Skills Lab  

            ---

            ## Why learn Python?
            There are many reasons why you should consider learning Python if you are aiming for a job 
            in the tech industry as a Data Analyst, Data Scientist, Machine Learning Engineer or Software 
            Developer.

            ### Popularity
            Python has been one of the most in-demand programming languages for many years. The [TIOBE index](https://www.tiobe.com/tiobe-index/)
            ranks Python on first position this year, ahead of languages like C, Java and C++.
            """
        )

        tiobe_top_20_url = "https://raw.githubusercontent.com/mwiemers/test_app/main/tiobe_top20.csv"
        tiobe_history_url = "https://raw.githubusercontent.com/mwiemers/test_app/main/tiobe_history.csv"
        gapminder_url = "https://raw.githubusercontent.com/mwiemers/test_app/main/gapminder.csv"

        tiobe_top_20 = clean_tiobe_top_20(load_data(tiobe_top_20_url))
        tiobe_history = clean_tiobe_history(load_data(tiobe_history_url))
        gap = load_data(gapminder_url)

        st.dataframe(tiobe_top_20, use_container_width = True)

        st.write("\n")
        st.markdown(
            """
            As you can see from the TIOBE historic data, Python has seen the strongest growth in popularity among 
            all programming languages across the past 5 years.
            """
        )

        fig = px.line(
            tiobe_history, 
            x='year', 
            y='rank', 
            color='language', 
            title='TIOBE historic data')

        fig.update_layout(yaxis_range=[40, 1])

        st.plotly_chart(fig, use_container_width=True)

        
        st.markdown(
            """
            ### Easy to learn
            One of the advantages of Python is that it is easy to learn due to it's simple syntax 
            and the vast amount of online resources in forms of tutorials, online courses and help 
            available thorugh online discussion forums like stackoverflow.

            Some of the best available resources to learn Python are:
            - [Dataquest](https://dataquest.io) (Learn Python for Data Science and Machine Learning)
            - [Codecademy](https://www.codecademy.com/) (Learn about the additional applications of Python outside the core Data Sience realm)
            - [Realpython](https://realpython.com/) (Similar to Codecademy, but only covers Python)
            - [Pythonmorsels](https://www.pythonmorsels.com/) (Polish your Python skills to write more pythonic and efficient code)

            """
        )
        st.write("\n")
        st.markdown(
            """
            ### Open Source
            Python is an open source progamming language, which means that the Python user community can 
            contribute to the development of Python by creating new 'libraries' for specific tasks.

            This dashboard/webapp, for instance, was developed with [streamlit](https://streamlit.io/).

            One of the best tools to develop animated and interactive charts is [plotly](https://plotly.com/) 
            and due to Python's popularity, a plotly can be used through Python as well.

            Below is an example of a beautiful chart, that was created with plotly, using only a few lines of code.

            Click the **play button** to start the animation!
            """
        )


        st.code(body=
        """
            fig = px.scatter(gap, x="gdp_pc", y="life_exp", color="continent", size='pop', animation_frame="year",
                            range_x=[0, 50000], 
                            range_y=[22, 90],
                            title="Gapminder",
                            hover_data=['country'],
                            labels={"gdp_pc":"GDP per capita",
                                    "life_exp":"Life Expectancy",
                                    "continent": "Continent"})
        """,
        language='python')

        fig = px.scatter(gap, x="gdp_pc", y="life_exp", color="continent", size='pop', animation_frame="year",
                        range_x=[0, 50000], 
                        range_y=[22, 90],
                        title="Gapminder",
                        hover_data=['country'],
                        labels={"gdp_pc":"GDP per capita",
                                "life_exp":"Life Expectancy",
                                "continent": "Continent"}
            )

        st.plotly_chart(fig, use_container_width=True)

        
        st.markdown(
                """
                ### Versatility
                Python is a general purpose programming language, which means that it was developed 
                to be used for all possible use-cases. It is the most popular language for Data Science together 
                with R, but can be applied for all kinds of purposes.

                Python is among the favourite languages for web applications. Below is a simple example of a simple 
                Finance dashboard that enbales the user to select stocks and plot their data

                """
            )

        dropdown = st.multiselect(
            'Choose a stock', 
            ['TSLA', 'MSFT', 'GOOG', 'FB', 'NFLX', 'AMZN', 'BTC-USD'],
            ['TSLA'])

        start = st.date_input('Start', value = pd.to_datetime('2019-01-01'))
        end = st.date_input('End', value = pd.to_datetime('today'))

        adj_close = web.DataReader(dropdown, 'yahoo', start, end)['Adj Close']
        returns = (adj_close.pct_change()+1).cumprod() - 1
        st.write('\n\n Stock Returns')
        st.line_chart(returns)

    if page == 'Learning Python with Dataquest':

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

    if page == 'The workshop format':

        st.title("The format of the Python sessions")



@st.cache
def load_data(url):
    return pd.read_csv(url)
    
    
def clean_tiobe_top_20(df):
    return (
        df
        .drop(columns=['Unnamed: 0', 'Sep 2021', 'Programming Language'])
        .rename(columns={'Sep 2022': 'Rank 2022',
                         'Programming Language.1': 'Programming Language'})
        .iloc[:, [1, 0, 2]]
        )

def clean_tiobe_history(df):
    return (
        df
        .drop(columns=['Unnamed: 0'])
        .set_index('Programming Language')
        .transpose()
        .rename_axis('', axis='columns')
        .reset_index()
        .rename(columns={'index': 'year'})
        .melt(id_vars='year')
        .rename(columns={'value': 'rank', '': 'language'})
        .sort_values(by=['year', 'rank'])
        .assign(rank = lambda df: df['rank'].replace({'-': np.nan}).astype('float'))
        .query("~language.isin(['Pascal', 'Visual Basic', '(Visual) Basic', 'Prolog'])", engine='python')
        )


if __name__ == '__main__':
    main()

