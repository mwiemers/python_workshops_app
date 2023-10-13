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
    2. Extracting the zip file.
        a. Windows: Right-click on the zip file and select extract all.
        b. Mac: Double-click on the zip file.
    3. Change the folder name to something meaningful like 'python_fundamentals'.

    ## Open Jupyter Lab
    
    ### On a teaching PC:
    1. Open the Anaconda prompt: Click the Windows key, type "Anaconda Prompt" and hit Enter
    2. In the Anaconda prompt, type in "H:" and hit Enter. This will change the drive to the H-drive, where the files have been downloaded.
    3. Still in the Anaconda prompt, type in "jupyter lab" and hit Enter. The jupyter lab app will launch in your browser after a few seconds.
    4. In jupyter lab, select the folder from the menu on the left side where you downloaded the notebook.
    5. Double-click on a notebook to open it.        
            
    ### On your personal laptop:
    1. Open the Anaconda prompt: 
            a. Windows: Click the Windows key, type "Anaconda Prompt" and hit Enter
            b. Mac: Use the Cmd+Space shortcut to open the Spotlight Search. Search for "Anaconda Prompt" and hit Enter.
    2. In the Anaconda prompt, type in "jupyter lab" and hit Enter. The jupyter lab app will launch in your browser after a few seconds.
    3. In jupyter lab, select the folder from the menu on the left side where you downloaded the notebook.
    4. Double-click on a notebook to open it.        
            
    """
)