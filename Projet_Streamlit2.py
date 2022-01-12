#!/usr/bin/env python
# coding: utf-8



#Import required libraries
import datetime
import numpy as np
import pandas as pd
import plotly as plt
import plotly.express as px
import streamlit as st



def app():
    #Loading the dataset
    file = ('C:/Users/HP/Downloads/portefeuille_EME.xlsx')
    my_data = pd.read_excel(file)
    #Convert column 'Cohorte' from datetime to date
    my_data["Cohorte"] = pd.to_datetime(my_data["Cohorte"]).dt.date
    my_data.head()

    #Adding dynamic filters
    st.sidebar.header('FILTERS')
    st.sidebar.markdown('Select the  characteristics of the plots')

    #Date filter
    cohorte = list(my_data['Cohorte'].drop_duplicates())
    cohorte_choice = st.sidebar.multiselect('Choose the month(s):', cohorte, default=cohorte)
    my_data = my_data[my_data['Cohorte'].isin(cohorte_choice)]

    #Manager filter
    manager = list(my_data['Manager'].drop_duplicates())
    manager_choice = st.sidebar.multiselect('Choose the manager(s):', manager, default=manager)
    my_data = my_data[my_data['Manager'].isin(manager_choice)]

    #City filter
    city = list(my_data['Site'].drop_duplicates())
    city_choice = st.sidebar.multiselect('Choose the city(s):', city, default=city)
    my_data = my_data[my_data['Site'].isin(city_choice)]

    #Image 4
    #PAGE 2
    #Fourth plot
    #st.markdown("In this page, I show you informations about end of service characteristics.")
    st.subheader('Number of customers finalized at 3 months')
    st.markdown("In tingari's services, we have deadline for completion of services. In this dataset, the deadline is three months.")
    chart_data = pd.DataFrame(my_data[["Finalisé à 3 mois","Customer"]].groupby(['Finalisé à 3 mois']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Finalisé à 3 mois':'index'}).set_index('index')
    st.bar_chart(chart_data)


    #Fifth plot
    st.subheader('Number of documents provided')
    st.markdown("To invoice customers, we need some documents like 'Charte adhésion bilan' and 'Émargement'.") 
    st.markdown("If we don't have them, we can't invoice them to Pôle Emploi.")
    chart_data = pd.DataFrame(my_data[["Charte adhésion - Bilan","Customer"]].groupby(['Charte adhésion - Bilan']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Charte adhésion - Bilan':'index'}).set_index('index')
    st.bar_chart(chart_data)

    #Sixth plot
    chart_data = pd.DataFrame(my_data[["Emargement","Customer"]].groupby(['Emargement']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Emargement':'index'}).set_index('index')
    st.bar_chart(chart_data)