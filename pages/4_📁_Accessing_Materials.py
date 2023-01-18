import streamlit as st


st.set_page_config(
    page_title='Python Workshop Format',
    page_icon='📁'
)

st.title("Accessing and opening Jupyter Notebooks")

st.markdown("""

    ## Access to Jupyter Notebooks

    The Jupyter Notebooks can be accessed on Teams from the DSL-Python-Workshops team.

    Follow these steps to join the team:

    1. Learners will need to go to the Teams page in MS Teams, which can be accessed from the sidebar on the left.
    2. Select the Join or create team option on the top right.
    3. Enter the team code zpsyi8f.

    <br>
    To download the jupyter notebooks:

    1. Select a channel from the left sidebar inside the DSL-Python-Workshops team. The series are ordered.
    2. Select the Files tab to access the jupyter notebooks.
    3. Select a notebook and click Download to download it onto your local machine.
    4. Please download the notebook in a folder on the H-drive. This is your personal shared drive, which is 
       accessible from every PC on campus.

    ## Open jupyter notebooks

    To open a jupyter notebook, you will need to launch the jupyter lab app.

    1. Open the Anaconda prompt (Click the Windows key and type in Anaconda Prompt and hit Enter).
    2. Switch to the H-drive by typing in H: and hit Enter.
    3. Type in jupyter lab and hit Enter.
    4. In the jupyter lab app, select the folder from the menu on the left side where you downloaded the notebook.
    5. Double-click on the notebook to open it.
    """
)