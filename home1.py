import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
import shap
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objects as go
import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
from PIL import Image
import plotly.express as px




def app():
    st.markdown(
            f"""
    <style>
        .reportview-container .main .block-container{{
           max-width: {1450}px;
        }}
        .reportview-container .main {{
            color: {'OffBlack'};
        }}
    </style>
    """,
            unsafe_allow_html=True,
        )

## Title
    st.image('/Users/user/Desktop/capstone/header1.jpg',width= 1450)
    st.markdown(f"<h1 style='text-align:center;' >{'<b>Career Guide Dashboard</b>'}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;' >{'by Luna Baalbaki, MSBA student at AUB'}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color: #639262;' >{'<b>Navigation</b>'}</h2>", unsafe_allow_html=True)
# skipping some lines
    st.write("")
    st.selectbox('Choose page', ('Home','Job Market Analysis in Lebanon', 'Job Information'))
    st.write("")
    st.write("")
    st.write("")

    st.image('/Users/user/Desktop/capstone/line_separator.png',width= 1450)


    st.markdown(f"<h2 style='text-align:left; font-family:arial;' >{'<b>Home</b>'} </h2>", unsafe_allow_html=True)
# st.markdown(f"<h2 style='text-align:center;' >{'Are you a Lebanese 🇱🇧  student struggling in choosing your career?'}</h2>", unsafe_allow_html=True)
#Load Data
    df1=pd.read_csv('/Users/user/Desktop/Capstone_datasets/preprocessed_linkedin_jobs_25_08_21.csv')
    df2=pd.read_csv('/Users/user/Desktop/Capstone_datasets/skill_importance.csv')
    df3=pd.read_csv('/Users/user/Desktop/Capstone_datasets/tasks.csv')
    df5=pd.read_csv('/Users/user/Desktop/Capstone_datasets/Detailed_work_activities_tasks.csv')
    df6=pd.read_csv('/Users/user/Desktop/Capstone_datasets/bright_oulook_onet.csv')



# st.markdown(f"<h2 style='text-align:left; font-family:arial' >{'<b>Job Analysis in Lebanon Based on LinkedIn Data</b>'}</h2>", unsafe_allow_html=True)

 ## Creating a page divider to improve design
    html_title_sec11= """
                <div style="background-color:#639262;padding:4px">
                <h2 style="color:white;text-align:center;"> Are you a Lebanese 🇱🇧  student struggling in choosing your career?</h2>
                </div>
                """
    html_title_sec2= """
                <div style="background-color:#77A675;padding:4px">
                <h2 style="color:white;text-align:center;"> Section II. Date and Location </h2>
                </div>
                """
    html_space1= """
                <div style="background-color:#77A675;padding:4px">
                <h2 style="color:OffBlack;text-align:center;"></h2>
                </div>
                """
    st.markdown(html_title_sec11, unsafe_allow_html=True)
    st.write("")
    st.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Selecting the right career is one of the most important decisions students have to make. With the increase in the number of career paths and opportunities, making this decision have become quite difficult. The purpose of this project is to do a job market analysis in Lebanon to provide information about different job trends in Lebanon up-to-date to Lebanese students, so they could form better career choices. Since many         Lebanese students don’t know which major to choose and which job position is highly demanded in Lebanon, this project guides them in their career choice.' }</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Datasets are taken from LinkedIn and O*net websites. You can check the datasets below:' }</h3>", unsafe_allow_html=True)


#Check Data
    if st.checkbox("Check Dataset: Jobs in Lebanon"):
        st.write(df1.head())
    if st.checkbox("Check Dataset: Skills"):
        st.write(df2.head())
    if st.checkbox("Check Dataset: Tasks"):
        st.write(df3.head())
    if st.checkbox("Check Dataset: Detailed Work Activities"):
        st.write(df5.head())


# #footer
# from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
# from htbuilder.units import percent, px
# from htbuilder.funcs import rgba, rgb
# def image(src_as_string, **style):
#     return img(src=src_as_string, style=styles(**style))
#
#
# def link(link, text, **style):
#     return a(_href=link, _target="_blank", style=styles(**style))(text)
#
#
# def layout(*args):
#
#     style = """
#     <style>
#       # MainMenu {visibility: hidden;}
#       footer {visibility: hidden;}
#      .stApp { bottom: 105px; }
#     </style>
#     """
#
#     style_div = styles(
#         position="fixed",
#         left=0,
#         bottom=0,
#         margin=px(0, 0, 0, 0),
#         width=percent(100),
#         color="black",
#         text_align="center",
#         height="auto",
#         opacity=1
#     )
#
#     style_hr = styles(
#         display="block",
#         margin=px(8, 8, "auto", "auto"),
#         border_style="inset",
#         border_width=px(2)
#     )
#
#     body = p()
#     foot = div(
#         style=style_div
#     )(
#         hr(
#             style=style_hr
#         ),
#         body
#     )
#
#     st.markdown(style, unsafe_allow_html=True)
#
#     for arg in args:
#         if isinstance(arg, str):
#             body(arg)
#
#         elif isinstance(arg, HtmlElement):
#             body(arg)
#
#     st.markdown(str(foot), unsafe_allow_html=True)
#
#
# def footer():
#     myargs = [
#
#         "by ",
#         link("https://github.com/lunabaalbaki?tab=repositories", "Luna Baalbaki"),
#         br(),
#         link("mailto:lab28@mail.aub.edu", "Send me an Email")
#
#     ]
#     layout(*myargs)
#
# if __name__ == "__main__":
#     footer()
