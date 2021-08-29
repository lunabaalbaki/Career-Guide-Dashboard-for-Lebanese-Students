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

#Load Data
df1=pd.read_csv('https://raw.githubusercontent.com/lunabaalbaki/Career-Guide-Dashboard-for-Lebanese-Students/main/preprocessed_linkedin_jobs_25_08_21.csv')
df2=pd.read_csv('https://raw.githubusercontent.com/lunabaalbaki/Career-Guide-Dashboard-for-Lebanese-Students/main/skill_importance.csv')
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


#Date
# month_ = list(df1["Month"].unique())
# product_date = []
# for i in month_:
#     x = df1[df1["Month"] == i]
#     sums = sum(x.Count)
#     product_date.append(sums)
#
# data = pd.DataFrame({"month_": month_, "product_date": product_date})
# new_index = (data["product_date"].sort_values(ascending=False)).index.values
# sorted_data = data.reindex(new_index)
# trace1 = go.Bar(
#                 x = sorted_data.month_,
#                 y = sorted_data.product_date,
#                 name = "Jobs Openings in Lebanon Over Months",
#                 marker = dict(color = '#5ce0a0',line = dict(color="rgb(2,65,0)",width=1)))
# data = [trace1]
# layout = dict(title = "Jobs Openings in Lebanon Over Months")
# fig11 = go.Figure(data = data, layout = layout)
# st.plotly_chart(fig11)

 ## Creating bar charts for customer demographics
# variable_selection = col1.selectbox('', ['accountant', 'actor'])
# fig1 = go.Figure()
# if variable_selection:
#     #fig1.add_trace(go.Bar(y= df_viz[variable_selection].value_counts(), x= df_viz[variable_selection]))
#     fig1.add_trace(go.Bar(y= df2['Importance'], x= df2['Skill']))
#     fig1.update_layout(title= 'Customers by {}'.format(variable_selection), yaxis_title='# of Customers', titlefont_size=24, template = 'plotly_white', xaxis={'categoryorder':'total descending'})
#     fig1.update_traces(marker_line_color='#008080',marker_line_width=1.5, opacity=0.6, hoverinfo = 'skip')
#     col3.plotly_chart(fig1)
#
# ## Adding customized insights per condition
# st.markdown(f"<h3 style='text-align:left; font-family:arial; color:Teal' >{'<b>Key Insight:</b>'}</h3>", unsafe_allow_html=True)
# if variable_selection == 'accountant':
#     mostfrequent_age_count = df2[df2['Profession']=='accountant'.value_counts()[0]
#     # mostfrequent_age_category = df_viz['Age Group'].value_counts().index[0]
#     st.subheader('luna'.format(mostfrequent_age_count))
# elif variable_selection == 'actor':
#     mostfrequent_job_count = df2[df2['Profession']=='actor'.value_counts()[0]
#     # mostfrequent_job_category = df_viz['Job Type'].value_counts().index[0]
#     st.subheader('**Currently, the majority ({})'.format(mostfrequent_job_count))
# st.subheader('**Currently, the majority ({}) of the bank\''.format(mostfrequent_ed_count)
# st.write("")
# st.write("")

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



#Hob Title
# with col3:
#     job_ = list(df1["Job Title"].unique())
#     product_job = []
#     for i in job_:
#         x = df1[df1["Job Title"] == i]
#         sums = sum(x.Count)
#         product_job.append(sums)
#
#     new_index = (data["product_job"].sort_values(ascending=False)).head(4).index.values
#     sorted_data = data.reindex(new_index)
#     trace1 = go.Bar(
#                   x = sorted_data.job_,
#                   y = sorted_data.product_job,
#                   name = "Most Required Job Positions in Lebanon",
#                   marker = dict(color = '#008080',line = dict(color="rgb(2,65,0)",width=1)))
# data = [trace1]
# layout = dict(title = "Most Required Job Positions in Lebanon")
# fig13 = go.Figure(data = data, layout = layout)
# st.plotly_chart(fig13)



    # col1.markdown(f"<h3 style='text-align:left; font-family:arial;' >{'Choose a Variable to Explore'}</h3>", unsafe_allow_html=True)


    ## Creating bar charts for customer demographics
    # variable_selection = col1.selectbox('Select a Profession:', df2['Profession'].unique())
    # fig1_ = go.Figure()
    # if variable_selection:
    #     #fig1.add_trace(go.Bar(y= df_viz[variable_selection].value_counts(), x= df_viz[variable_selection]))
    #     fig1_.add_trace(go.Bar(y= df2['Importance'], x= df2[df2['Profession'].str.contains(variable_selection)]))
    #     fig1_.update_layout(title= 'Customers by {}'.format(variable_selection), yaxis_title='# of Customers', titlefont_size=24, template = 'plotly_white', xaxis={'categoryorder':'total descending'})
    #     fig1_.update_traces(marker_line_color='#008080',marker_line_width=1.5, opacity=0.6, hoverinfo = 'skip')
    #     col3.plotly_chart(fig1_)

        ## Adding customized insights per condition
    # st.markdown(f"<h3 style='text-align:left; font-family:arial; color:Teal' >{'<b>Key Insight:</b>'}</h3>", unsafe_allow_html=True)
    # if variable_selection == 'accountant':
    #     mostfrequent_age_count = df1['Age Group'].value_counts()[0]
    #     mostfrequent_age_category = df_viz['Age Group'].value_counts().index[0]
    #     st.subheader('**Currently, the majority ({}) of the bank\'s customers are {}**'.format(mostfrequent_age_count,mostfrequent_age_category))
    # elif variable_selection == 'Job Type':
    #     mostfrequent_job_count = df_viz['Job Type'].value_counts()[0]
    #     mostfrequent_job_category = df_viz['Job Type'].value_counts().index[0]
    #     st.subheader('**Currently, the majority ({}) of the bank\'s customers have the {} job type**'.format(mostfrequent_job_count,mostfrequent_job_category))
    # elif variable_selection == 'Wealth Bracket':
    #     mostfrequent_wealth_count = df_viz['Wealth Bracket'].value_counts()[0]
    #     mostfrequent_wealth_category = df_viz['Wealth Bracket'].value_counts().index[0]
    #     st.subheader('**Currently, the majority ({}) of the bank\'s customers are in the {} wealth bracket**'.format(mostfrequent_wealth_count,mostfrequent_wealth_category))
    # elif variable_selection == 'Education Level':
    #     mostfrequent_ed_count = df_viz['Education Level'].value_counts()[0]
    #     mostfrequent_ed_category = df_viz['Education Level'].value_counts().index[0]
    # st.subheader('**Currently, the majority ({}) of the bank\'s customers have a {} education level**'.format(mostfrequent_ed_count,mostfrequent_ed_category))
    # st.write("")
    # st.write("")
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


with col3:
    #st.subheader('Most Demanded Job Positions in Lebanon')
    df_sk = st.selectbox('Select a City:', df1['Location'].unique())
    det45= df1[df1['Location'].str.contains(df_sk)]
    industop_ = list(det45["Category"].unique())
    industry_top = []
    for i in industop_:
        x = det45[det45["Category"] == i]
        sums = sum(x.Count)
        industry_top.append(sums)

    data = pd.DataFrame({"industop_": industop_, "industry_top": industry_top})
    new_index = (data["industry_top"].sort_values(ascending=False)).head(8).index.values
    sorted_data = data.reindex(new_index)
    trace1 = go.Bar(
                   x = sorted_data.industop_,
                   y = sorted_data.industry_top,
                   name = "Most Demanded Job Positions in Lebanon",
                   marker = dict(color = '#77A675',line = dict(color="rgb(2,65,0)",width=1.5)))
    data = [trace1]
    layout = dict(title = " ")
    fig91 = go.Figure(data = data, layout = layout)
    fig91.update_layout(title= 'Most Demanded Jobs Based on Cities in Lebanon', yaxis_title='# of Jobs', titlefont_size=24, template = 'plotly_white', xaxis_title= 'Job Positions')
    col3.plotly_chart(fig91)


#NEW







# with col3:
#     st.subheader('Lowest 5 Industries with least Job Openings')
#     industop_ = list(df4["Industry"].unique())
#     industry_top = []
#     for i in industop_:
#         x = df4[df4["Industry"] == i]
#         sums = sum(x.Count)
#         industry_top.append(sums)
#
#     data = pd.DataFrame({"industop_": industop_, "industry_top": industry_top})
#     new_index = (data["industry_top"].sort_values(ascending=True)).head(5).index.values
#     sorted_data = data.reindex(new_index)
#     trace1 = go.Bar(
#                   x = sorted_data.industop_,
#                   y = sorted_data.industry_top,
#                   name = "Least Job Openings Industries in Lebanon",
#                   marker = dict(color = '#008080',line = dict(color="rgb(2,65,0)",width=1.5)))
# data = [trace1]
# layout = dict(title = " ")
# fig92 = go.Figure(data = data, layout = layout)
# col3.plotly_chart(fig92)

###############
# least_ind_jobs = df4['Industry'].value_counts()[10]
# col3.subheader('The indusrty with the least job openings is **Insurance**. It has **30** job openings.')



#Companies

# with col3:
#     st.subheader('Top Job positions in Demand in Lebanon')
#
#     industop = list(df1["Job Title"].unique())
#     industrytop = []
#     for i in industop:
#         x = df1[df1["Job Title"] == i]
#         sums = sum(x.Count)
#         industrytop.append(sums)
#
#     data = pd.DataFrame({"industop": industop, "industrytop": industrytop})
#     new_index = (data["industrytop"].sort_values(ascending=False)).head(7).index.values
#     sorted_data = data.reindex(new_index)
#     trace1 = go.Bar(
#                    x = sorted_data.industop,
#                    y = sorted_data.industrytop,
#                    name = "Top Job positions in Demand in Lebanon",
#                    marker = dict(color = '#008080',line = dict(color="rgb(2,65,0)",width=1.5)))
#     data = [trace1]
#     layout = dict(title = " ")
#     fig96 = go.Figure(data = data, layout = layout)
#     col3.plotly_chart(fig96)



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
