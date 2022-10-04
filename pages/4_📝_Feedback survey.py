import streamlit as st

st.set_page_config(
    page_title="Give us your Feedback!",
    page_icon="📝"
)


st.title("Fill in the survey to let us know your feedback about the Python workshops")

st.markdown(
    """
    We are piloting using Dataquest for our regular Python workshops this term and would highly 
    appreciate your feedback and suggestions on how we can improve these workshops.  
      
    Please use [this link](https://lse.eu.qualtrics.com/jfe/form/SV_ewXuHQ1nRnurTdY?topic=Python&coursename=Python%20for%20Data%20Science&version=22-23&prog=DS) 
    to submit your response.
    """)