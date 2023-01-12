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
    page_title='Installing Python',
    page_icon="💻"
)


st.markdown("""
    # Chosing an installation

    There are three main options to install Python on your PC:
    1) Python
    2) Anaconda
    3) Miniconda

    The main reason why you might want to choose Anaconda or Miniconda, is because of the greater ease with which you can manage environments compared to Python as such.

    ## What are environments and why should you care?

    We first need to understand what environments are and why they matter. In programming it is important that you can create separate workspaces called environments to work with a 
    specific collection of libraries. A library is a complex collection of tools (functions and classes) to perform specific tasks like data manipulation, visualization, analysis, 
    machine learning and deep learning. Libraries depend on other libraries. This can potentially create conflifts where two libraries that you need for different projects 
    require a different version of a third library. To solve such a dependency conflict, we need to create two separate workspaces or environments. In environment 1, library A 
    can work with version 1 of library C. In environment 2, library B can work with version 2 of library C.

    Below is an example of this problem. Let's assume you have a data science project and a web application project. For the Data Science project you need a specific data wrangling 
    library. This data wrangling library itself needs a specific Python version and a specific numpy version. For your web application project you need a specific web development 
    library. This web development library itself needs a Python version and numpy version that is different from the version your data wranling library needs. The problem is that in a 
    single environment we can only have one version of a specific library. You will have to chose whether to use the Python and Numpy version that is required for the data wrangling or 
    the web development library.

"""
)
image = load_image('https://www.dropbox.com/s/a49jvvktzu4xizp/managing_environments.svg?raw=1')
st.image(image, caption='Managing environments')

st.markdown("""

    ## Managing libraries and environments with Anaconda vs Python

    To solve this problem, we therefore need multiple environments. To work on our data science project, we create a data-science-environment, where we can work with the data wrangling library
    which uses Python version 3.10 and NumPy version 1.2.4. To work on our web app project, we create a web-dev-environment, where we can work with the web development library
    which uses Python version 2.7 and NumPy version 1.1.0. 

    This might look complicated, but it basically just means that we create separate independent Python versions on our computer for different projects, with different libraries installed 
    in these separate environments.

    This process of creating separate Python versions for different projects to avoid library dependency problems is easier with Anaconda than it is with just Python. Anaconda
    comes with conda, which is a package *and* environment management system (you can think of the term package as just being a different name for library at this point). This means 
    with conda we can install/remove libraries *and* create/remove and manage environments! In Python we need pip to install/remove libraries and venv to create/remove and manage 
    environments. Creating environments with the pre-installed Python version is a simple process using venv and pip. However, if you want to create a new environment with 
    a different Python version, you will need to use yet another tool to download and it turns out that the whole process is not always very straightforward, especially if you are using 
    a Windows machine.

    **The simplicity of the installation with Anaconda and the fact that we can use conda to manage both libraries and environments with different Python versions is the reason
     why we recommend it for beginners.**
""")

st.markdown("""
    ## Anaconda vs Miniconda

    ### Anaconda
    Anaconda is a Python distribution, i.e. a software bundle consisting of Python libraries (pandas, numpy, matplotlib and many more) and 
    software to write Python code (Jupyter, Spyder, VS Code,...). At its root stands the conda package and environment manager, which enables you to download Python libraries
    and create separate environments to store libraries in. It is important to understand the distinction between the conda package manager and the Anaconda distribution 
    that adds lots of software and libraries on top of it. 

    With Anaconda, conda and all the additional software will be installed on your computer. This is convenient for a beginner since you do not have to worry about installing 
    Jupyter Lab and Juypter Notebooks and maybe even VS Code to write your Python scripts. You also will have a large collection of libraries ready to start working with Python 
    from the start.

    ### Miniconda
    If you want a leaner setup and know which software you want to use to write code, you might want to opt for Miniconda instead. Miniconda only installs conda which comes 
    with a base Python environment that has no additional libraries for data science pre-installed. See the next sections on IDE's we recommend to write Python code and 
    how to use conda commands to manage libraries and environments.
""")

image = load_image('https://www.dropbox.com/s/djz5usz309cbhy8/anaconda_miniconda.svg?raw=1')
st.image(image, caption='Anaconda vs Miniconda')

st.markdown("""
    ## Best Python Data Science IDE's

    All of these IDE's support conda environments.

    ### Jupyter Lab/Notebooks
    Jupyter Lab and Notebooks is a web application running in your browser. That means, you will work with these apps in a browser tab. While a classical programming script is nothing 
    more than a plain text file, jupyter notebooks are much more than that. A notebook can contain sections for text, images and code and plots. The text sections can be formatted 
    with markdown or html code to improve their appearance. Once you got to know how to use them, you will find that notebooks offer a very convenient way to write reports 
    on data science projects, which is why we only recommend IDE's that support jupyter notebooks.

    The main difference between Jupyter Notebook and Jupyter Lab is that the latter is more powerful and can be customized in many ways. In addition, in jupyter labs you can easily 
    navigate your folders and select files in the side pane and have multiple notebooks open in the same browser tab.

    ### VS Code
    Although technically not a full-fledged IDE, VS code offers many tools that make it a great choice to write Python code and Jupyter Notebooks. It requires a bit of setting up
    though to be able to use it with Python and jupyter notebooks. The main advantages over Jupyter Lab is the fact that if offers a code editor to edit normal Python scripts, 
    which jupyter lab does not provide at the moment and can be used to write code in many languages.

    ### DataSpell
    DataSpell is IDE specifically designed for Data Science. While it is very similar in its capabilities to VS Code its looks and features are somewhat more polished and work 
    more seamless. Since you can get a free licence as a student or teacher, you might want to give it a try. But be aware that you will have to pay for it once you are no longer 
    a student and the price tag is quite significant.

""")

st.markdown("""
    ## Using conda

    ### Installing libraries

    **Installing the pandas library.**

    ```
    conda install pandas
    ```

    **Installing a specific version of pandas.**
    ```
    conda install pandas=1.4
    ```

    **Installing pandas from the conda-forge channel.** You can think of a channel as a separate website from where to download libraries. Some libraries are only available from certain 
    channels. You can specify the channel to look for the library, using the -c flag followed by the channel name, which is conda-forge in this case.
    ```
    conda install -c conda-forge pandas
    ```


    ### Managing environments

    **Creating a new environment with the base Python version**
    ```
    conda create --name data-science
    ```

    **Creating a new environment with a specific Python version**
    ```
    conda create --name data-science python=3.7
    ```

    **Activating an environment**. Unless you switch to an environment, the base environment will be active. Use this command to switch to the an environment named data-science.
    ```
    conda activate data-science
    ```

    **Deactivating an environment**. Deactivating will move you back to the base environment.
    ```
    conda deactivate
    ```

    **Get an overview of all environments**. The currently active environment is indicatd by the asterisk symbol.
    ```
    conda env list
    ```

    **Get an overview of all libraries in the activated environment**. 
    ```
    conda list
    ```

    **Remove an environment**. You might have misconfigured your environment and want to start from scratch. Use this command to remove the data-science environment.
    ```
    conda env remove -n data-science
    ```



    ### Installing Jupyter and Juypter Lab
    If you are creating a new environment, you need to also install jupyter in it, otherwise you will not be able to write jupyter notebooks inside the specific environment.
    Make sure you have the correct environment active before running the install command.

    ```
    conda install notebook jupyterlab
    ```

    To enable extensions in jupyter lab, you also need to install node.js
    ```
    conda install -c conda-forge nodejs
    ``` 

""")


