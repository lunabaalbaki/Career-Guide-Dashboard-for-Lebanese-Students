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
# st.markdown(f"<h2 style='text-align:center; color: #639262;' >{'<b>Navigation</b>'}</h2>", unsafe_allow_html=True)
# skipping some lines
st.write("")
# st.selectbox('Choose page', ('Home','Job Market Analysis in Lebanon', 'Job Information'))

nav= st.selectbox("Navigation", ["Home", "Job Market Analysis in Lebanon", "Job Information"])
st.write("")
st.write("")
st.image('/Users/user/Desktop/capstone/line_separator.png',width= 1450)



# st.markdown(f"<h2 style='text-align:center;' >{'Are you a Lebanese 🇱🇧  student struggling in choosing your career?'}</h2>", unsafe_allow_html=True)
#Load Data
df1=pd.read_csv('/Users/user/Desktop/Capstone_datasets/preprocessed_linkedin_jobs_25_08_21.csv')
df2=pd.read_csv('/Users/user/Desktop/Capstone_datasets/skill_importance.csv')
df3=pd.read_csv('/Users/user/Desktop/Capstone_datasets/tasks.csv')
df5=pd.read_csv('/Users/user/Desktop/Capstone_datasets/Detailed_work_activities_tasks.csv')
df6=pd.read_csv('/Users/user/Desktop/Capstone_datasets/bright_oulook_onet.csv')



# st.markdown(f"<h2 style='text-align:left; font-family:arial' >{'<b>Job Analysis in Lebanon Based on LinkedIn Data</b>'}</h2>", unsafe_allow_html=True)

 ## Creating a page divider to improve design


if nav == "Home":
    st.markdown(f"<h2 style='text-align:left; font-family:arial;' >{'<b>Home</b>'} </h2>", unsafe_allow_html=True)
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


if nav == "Job Market Analysis in Lebanon":
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

 ## Creating a page divider to improve design
    html_title_sec1= """
                <div style="background-color:#639262;padding:4px">
                <h2 style="color:white;text-align:center;"> Section I. Data Scrapped Information </h2>
                </div>
                """
    html_title_sec2= """
                <div style="background-color:#639262;padding:4px">
                <h2 style="color:white;text-align:center;"> Section II. Job Market Analysis in Lebanon - Locations & Companies </h2>
                </div>
                """
    html_title_sec3= """
                <div style="background-color:#639262;padding:4px">
                <h2 style="color:white;text-align:center;"> Section III. Job Market Analysis in Lebanon - Job Openings </h2>
                </div>
                """
    html_space1= """
                <div style="background-color:#77A675;padding:4px">
                <h2 style="color:OffBlack;text-align:center;"></h2>
                </div>

              """

    st.write("")
    st.markdown(f"<h2 style='text-align:left; font-family:arial;' >{'<b>Job Market Analysis in Lebanon</b>'} </h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'This section explores different job trends in Lebanon based on LinkedIn data. The dataset was scrapped from LinkedIn website. The dataset collected from LinkedIn contains information about the job title, location, company name and date posted. The Data was collected on 23/08/2021' }</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    col1,col2,col3,col4,col5 = st.beta_columns([30,5,30,5,30])

    st.markdown(html_title_sec1, unsafe_allow_html=True)
# col1.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Choose a Variable to Explore'}</h3>", unsafe_allow_html=True)



    col1,col2,col3,col4= st.beta_columns([30,10,30,10])

    with col1:

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    with col1:
        nb_jobs = len(df1)
        st.markdown(f"<h2 style='text-align:center; font-family:arial; color: black;' >{'<b>Number of Scrapped Jobs</b>'} </h2>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align:center; color: offblack;' >{nb_jobs} </h1>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align:center; font-family:arial; color: black;' >{'These job positions were scrapped from LinkedIn'} </h4>", unsafe_allow_html=True)

        ####


    with col3:
    #st.subheader('Jobs Postings in Lebanon Over Months')
        mnth_ = list(df1["Month"].unique())
        month_top = []
        for i in mnth_:
            x = df1[df1["Month"] == i]
            sums = sum(x.Count)
            month_top.append(sums)

        data = pd.DataFrame({"mnth_": mnth_, "month_top": month_top})
        new_index = (data["month_top"].sort_values(ascending=False)).index.values
        sorted_data = data.reindex(new_index)
        trace1 = go.Bar(
                      x = sorted_data.mnth_,
                      y = sorted_data.month_top,
                      name = "Data Scrapped Contains Jobs from the Following Months",
                      marker = dict(color = '#77A675',line = dict(color="rgb(2,65,0)",width=1.5)))
    data = [trace1]
    layout = dict(title = " ")
    fig97 = go.Figure(data = data, layout = layout)
    fig97.update_layout(title= 'Dataset Contains Jobs from the Following Months', yaxis_title='# of Jobs', titlefont_size=24, template = 'plotly_white', xaxis_title= 'Month')
    col3.plotly_chart(fig97)
#####

    st.markdown(html_title_sec2, unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")

    col1,col2,col3,col4= st.beta_columns([30,10,30,10])

    with col1:
        st.subheader('Job Openings in Lebanon Based on Location')
## Pie Chart Showing the Proportion of Customers with Personal Loans
        fig0 = go.Figure()
        color_list = ['#77A675', 'lightgray']
        fig0.add_trace(go.Pie(labels= df1['Location'], values= df1['Count']))
        fig0.update_traces(hoverinfo='label+percent', textinfo='label+percent',insidetextorientation='radial', textfont_size=14, marker=dict(colors= color_list, line=dict(color='#FFFFFF', width=2)))
        st.plotly_chart(fig0)

    with col3:
    # st.subheader('Top Hiring Companies in Lebanons')
        company_ = list(df1["Company"].unique())
        product_profit = []
        for i in company_:
            x = df1[df1["Company"] == i]
            sums = sum(x.Count)
            product_profit.append(sums)

        data = pd.DataFrame({"company_": company_, "product_profit": product_profit})
        new_index = (data["product_profit"].sort_values(ascending=False)).head(7).index.values
        sorted_data = data.reindex(new_index)
        trace1 = go.Bar(
                      x = sorted_data.company_,
                      y = sorted_data.product_profit,
                      name = "Top Hiring Companies in Lebanon",
                      marker = dict(color = '#77A675',line = dict(color="rgb(2,65,0)",width=1.5)))
    data = [trace1]
    layout = dict(title = " ")
    fig12 = go.Figure(data = data, layout = layout)
    fig12.update_layout(title= 'Top Hiring Companies in Lebanon', yaxis_title='# of Jobs', titlefont_size=24, template = 'plotly_white', xaxis_title= 'Company')
    col3.plotly_chart(fig12)
    comp_jobs = df1['Company'].value_counts()[0]






    st.markdown(html_title_sec3, unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
###
    col1,col2,col3,col4= st.beta_columns([30,10,30,10])
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        industop_ = list(df1["Category"].unique())
        industry_top = []
        for i in industop_:
            x = df1[df1["Category"] == i]
            sums = sum(x.Count)
            industry_top.append(sums)

        data = pd.DataFrame({"industop_": industop_, "industry_top": industry_top})
        new_index = (data["industry_top"].sort_values(ascending=False)).head(12).index.values
        sorted_data = data.reindex(new_index)
        trace1 = go.Bar(
                       x = sorted_data.industop_,
                       y = sorted_data.industry_top,
                       name = "Most Demanded Job Positions in Lebanon",
                       marker = dict(color = '#77A675',line = dict(color="rgb(2,65,0)",width=1.5)))
        data = [trace1]
        layout = dict(title = " ")
        fig91 = go.Figure(data = data, layout = layout)
        fig91.update_layout(title= 'Most Demanded Job Positions in Lebanon', yaxis_title='# of Jobs', titlefont_size=24, template = 'plotly_white', xaxis_title= 'Job Positions')
        col1.plotly_chart(fig91)

        st.markdown(html_space1,unsafe_allow_html=True)

if nav == "Job Information":
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

#Table
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
