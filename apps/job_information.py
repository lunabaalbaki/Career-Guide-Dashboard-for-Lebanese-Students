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
import altair as alt
#Load Data
df1=pd.read_csv('/Users/user/Desktop/Capstone_datasets/preprocessed_linkedin_jobs_25_08_21.csv')
df2=pd.read_csv('/Users/user/Desktop/Capstone_datasets/skill_importance.csv')
df3=pd.read_csv('/Users/user/Desktop/Capstone_datasets/tasks.csv')
df5=pd.read_csv('/Users/user/Desktop/Capstone_datasets/Detailed_work_activities_tasks.csv')
df6=pd.read_csv('/Users/user/Desktop/Capstone_datasets/bright_oulook_onet.csv')
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


st.write("")
st.markdown(f"<h2 style='text-align:left; font-family:arial;' >{'<b>Job Information Guide</b>'} </h2>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'This section explores different job professions. It provides detailed information about different job professions. It provides skills, tasks and detailed work activities for each job profession. This section helps students be more knowledgable about different professions. This data is collected from O*net website on 23/08/2021.' }</h3>", unsafe_allow_html=True)
st.write("")
st.write("")

 ## Creating a page divider to improve design
html_title_sec11= """
            <div style="background-color:#639262;padding:4px">
            <h2 style="color:white;text-align:center;"> Section I. Tasks & Bright Outlook </h2>
            </div>
            """
html_title_sec21= """
            <div style="background-color:#639262;padding:4px">
            <h2 style="color:white;text-align:center;"> Section II. Skills </h2>
            </div>
            """
html_title_sec31= """
            <div style="background-color:#639262;padding:4px">
            <h2 style="color:white;text-align:center;"> Section III. Detailed Work Activity </h2>
            </div>
            """
html_space1= """
            <div style="background-color:#639262;padding:4px">
            <h2 style="color:OffBlack;text-align:center;"></h2>
            </div>

          """


tabke_task = st.beta_container()
with tabke_task:
    st.markdown(html_title_sec11, unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    col1,col2,col3,col4,col5 = st.beta_columns([30,5,30,5,30])
    col1.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Select a Profession'}</h3>", unsafe_allow_html=True)









#Check Data
# # Table for skills
# interactive = st.beta_container()
# with interactive:
df_task = st.selectbox(' ', df3['Profession'].unique())
det= df3[df3['Profession'].str.contains(df_task)]
fig01 = go.Figure(data=go.Table(
    header=dict(values=list(det[['Task']]),
        fill_color='#639262',
        align='center'),
    cells=dict(values=[det[['Task']]],
        fill_color= '#E5ECF6',
        align='left')))
fig01.update_layout(margin=dict(l=5,r=5,b=10,t=10))
fig01.update_layout(width=1300,height=500)
    #     paper_bgcolor=background_color)
st.write(fig01)

##



st.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Check if the profession that you are looking for has future rapid growth of numerous job openings or neither'}</h3>", unsafe_allow_html=True)
## Bright bright_outlook_onet
df_outlook = st.selectbox('Select a Profession:', df6['Professions'].unique())
deto= df6[df6['Professions'].str.contains(df_outlook)]
figo1 = go.Figure(data=go.Table(
    cells=dict(values=[deto[['Category for Bright Outlook']]],
        fill_color= '#E5ECF6',
        align='left')))
figo1.update_layout(margin=dict(l=5,r=5,b=10,t=10))
figo1.update_layout(width=1300,height=100)
    #     paper_bgcolor=background_color)
st.write(figo1)


tabke_task = st.beta_container()
with tabke_task:
    st.markdown(html_title_sec21, unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    col1,col2,col3,col4,col5 = st.beta_columns([30,5,30,5,30])
    col1.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Choose a Variable to Explore'}</h3>", unsafe_allow_html=True)

df_sk = st.selectbox('Select a Profession:', df2['Profession'].unique())
det45= df2[df2['Profession'].str.contains(df_sk)]
fig341 = go.Figure(data=go.Bar(
                               x = det45['Skill'],
                               y=  det45['Importance_n'],
                               name = "Skill Category by Importance",
                               marker = dict(color = '#639262',line = dict(color="rgb(2,65,0)",width=1))))
fig341.update_layout(margin=dict(l=5,r=5,b=10,t=10))
fig341.update_layout(width=1000,height=400)
    #     paper_bgcolor=background_color)
st.write(fig341)
# df_task = st.selectbox('Select wedwdkn a Profession:', df3['Profession'].unique())
# # st.write(df3[df3['Profession'].str.contains(df_task)])
# det= df3[df3['Profession'].str.contains(df_task)]
# st.write(det[['Task']])


# # Table for skills
# interactive = st.beta_container()
# with interactive:
# fig01 = go.Figure(data=go.Table(
#     header=dict(values=list(det[['Task']]),
#         fill_color='#FD8E72',
#         align='center'),
#     cells=dict(values=[det[['Task']]],
#         fill_color= '#E5ECF6',
#         align='left')))
# fig01.update_layout(margin=dict(l=5,r=5,b=10,t=10))
#     #     paper_bgcolor=background_color)
# st.write(fig01)

########
### MULTISELECT
# country_name_input = st.multiselect(
# 'Profession name',
# df2.groupby('Profession').count().reset_index()['Profession'].tolist())
#
# # by country name
# len(country_name_input) > 0
# subset_data = df2[df2['Profession'].isin(country_name_input)]




########################################################################################
## linechart

# st.subheader('Importance of Skills')
#
# total_cases_graph  =alt.Chart(subset_data).transform_filter(
#     alt.datum.Importance_n > 35
# ).mark_bar().encode(
#     x=alt.X('Skill', type='nominal', title='Skill', sort=alt.EncodingSortField(field='Order',order='descending')),
#     y=alt.Y('Importance_n',  title='Importance'),
#     color='Profession',
#     tooltip = 'sum(Importance_n)',
# ).properties(
#     width=1000,
#     height=500
# ).configure_axis(
#     labelFontSize=15,
#     titleFontSize=20
# )
# st.altair_chart(total_cases_graph)


###
####
tabke_task = st.beta_container()
with tabke_task:
    st.markdown(html_title_sec31, unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    col1,col2,col3,col4,col5 = st.beta_columns([30,5,30,5,30])
    col1.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Select a Profession'}</h3>", unsafe_allow_html=True)

#Detailed Work Activity Table
df_detailed = st.selectbox('.', df5['Profession'].unique())
det2= df5[df5['Profession'].str.contains(df_detailed)]
fig021 = go.Figure(data=go.Table(
    header=dict(values=list(det2[['Detailed Work Activity']]),
        fill_color='#639262',
        align='center'),
    cells=dict(values=[det2[['Detailed Work Activity']]],
        fill_color= '#E5ECF6',
        align='left')))
fig021.update_layout(margin=dict(l=5,r=5,b=10,t=10))
fig021.update_layout(width=1300,height=500)
    #     paper_bgcolor=background_color)
st.write(fig021)


#footer
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [

        "by ",
        link("https://github.com/lunabaalbaki?tab=repositories", "Luna Baalbaki"),
        br(),
        link("mailto:lab28@mail.aub.edu", "Send me an Email")

    ]
    layout(*myargs)

if __name__ == "__main__":
    footer()
