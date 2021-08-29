import streamlit as st

def app():

    ## Making an About Section
    st.markdown(f"<h2 style='text-align:left; font-family:arial;' >{'<b>About</b>'} </h2>", unsafe_allow_html=True)

    st.subheader("""
    Welcome! This Web App is a decision making tool intended to increase the accessibility of data-driven insights to key decision makers of a bank, primarily those in the marketing department. Although this particular application is based on a Portuguese bank's dataset, the template demonstrated here is transferrable to multiple use cases, within the Banking Industry or otherwise.
            """)

    st.write("")
    st.write("")
    st.write("")

    st.write("""
    Dataset Source: [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, In press, http://dx.doi.org/10.1016/j.dss.2014.03.001
    """)
