import streamlit as st


st.set_page_config(
    page_title='Opening Jupyter Lab',
    page_icon='📁'
)

st.title("Opening Jupyter notebooks in Juypter Lab")

st.markdown("""
            
    ## Extract the zip file
            
    Before you can open the jupyter notebooks, please ensure that you have extracted the files!
            
    1. Go to the folder where you downloaded the zip file (presumably your Downloads folder).
    2. Right-click on the zip file and select extract all.
    3. Change the folder name to something meaningful like 'python_fundamentals'.

    ## Open Jupyter Lab
            
    1. Open the Anaconda prompt: Click the Windows key and type in Anaconda Prompt and hit Enter
    2. Switch to the H-drive by typing in H: and hit Enter.
    3. Type in jupyter lab and hit Enter. The jupyter lab app will launch in your browser after a few seconds.
            
    ## Opening a jupyter notebook
    1. In the jupyter lab app, select the folder from the menu on the left side where you downloaded the notebook.
    2. Double-click on a notebook to open it.        

    """
)