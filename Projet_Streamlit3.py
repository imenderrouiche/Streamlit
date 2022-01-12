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
   
   #Image 5
    #PAGE 3
    #Seventh plot
    #st.markdown("Finally, I present you informations about customer invoicing.")
    st.subheader('Customer invoicing')
    st.markdown("Here, we present you the customer invoicing.") 
    chart_data = pd.DataFrame(my_data[["Facturation obtenue","Customer"]].groupby(['Facturation obtenue']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Facturation obtenue':'index'}).set_index('index')
    st.bar_chart(chart_data)

    st.markdown("Here, we present you the type of customer invoicing.")
    st.markdown("PAD DE FACTURATION = customers who haven't billing. Either their invoicing is pending, or we are not awaiting invoicing.")
    st.markdown("EXCLUS DE FACTURATION - 0% = customers who haven't subscribed to the service. Billed at 15% of the total amount.")
    st.markdown("N'A PAS ADHERE - 15% = customers who can no longer be billed (deadlines exceeded, missing documents, etc). Billed at 0% of the total amount.")
    st.markdown("SORTIE ANTICIPEE/ABANDON - 15% = customers who subscribed to the service but who dropped out during the service. Billed at 15% of the total amount.")
    st.markdown("FIN DE PRESTATION/ARRÊT DU PROJET (NON OPPORTUNE) - 100% = customers who complete the service but who don't pursue their professional project. Billed at 100% of the total amount.")
    st.markdown("FIN DE PRESTATION/ARRÊT DU PROJET (OPPORTUNE) - 100% = customers who complete the service and who pursue their professional project. Billed at 100% of the total amount.")
    chart_data = pd.DataFrame(my_data[["Type facturation","Customer"]].groupby(['Type facturation']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Type facturation':'index'}).set_index('index')
    st.bar_chart(chart_data)


    #Image 6
    #Conclusion
    st.subheader('Conclusion')
    st.markdown("So ends the presentation of youtube data analysis. I hope you liked it.")