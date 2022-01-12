#!/usr/bin/env python
# coding: utf-8

#Import different pages
import Projet_Streamlit1
import Projet_Streamlit2
import Projet_Streamlit3
import streamlit as st

#Add a title and an icon in the page
st.set_page_config(page_title='Tingari customer analysis', page_icon='📊')
#Add my personnal information
st.sidebar.header('ABOUT ME')
st.sidebar.markdown('Imen DERROUICHE')
st.sidebar.markdown('LinkedIn: Imen Derrouiche')
st.sidebar.markdown('GitHub: imenderrouiche')

#Pages name
PAGES = {
    "Customer Analysis": Projet_Streamlit1,
    "Service characteritics": Projet_Streamlit2,
    "Customer Invoicing": Projet_Streamlit3
}


#Set sidebar
#Image 1
st.sidebar.header('CONTENTS')
selection = st.sidebar.selectbox("", list(PAGES.keys()))
page = PAGES[selection]
page.app()