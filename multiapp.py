"""Frameworks for running multiple Streamlit applications as a single app.
"""

import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        ## Styling the Navigation Bar, using HTML to center the text, and using beta_columns to center the navigation bar
        st.markdown(f"<h2 style='text-align:center; color: Teal;' >{'<b>Navigation</b>'}</h2>", unsafe_allow_html=True)
        col1,col2,col3 = st.beta_columns(3)
        with col2:
            app = st.selectbox(
                '',
                self.apps,
                format_func=lambda app: app['title'])
        st.image('/Users/user/Desktop/capstone/header1.jpg',width= 1450)
        app['function']()
