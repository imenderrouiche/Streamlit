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

    #Adding dynamic filters
    #Image 2
    st.sidebar.header('FILTERS')
    st.sidebar.markdown('Select the  characteristics of the plots')

    #Loading the dataset
    file = ('C:/Users/HP/Downloads/portefeuille_EME.xlsx')
    my_data = pd.read_excel(file)
    #Convert column 'Cohorte' from datetime to date
    my_data["Cohorte"] = pd.to_datetime(my_data["Cohorte"]).dt.date
    my_data.head()

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



    #PAGE 1
    #Content of my dashboard
    #Title of my dashboard
    st.title('Tingari customer analysis')

    #Description of my dashboard
    st.markdown('In this dashboard, I will present Tingari data. Tingari is a consulting firm where I realize my stage.')
    st.markdown('Indeed, Tingari offers training in collaboration with Pôle Emploi.')
    st.markdown('I will try to show you informations about our customers.')
    #st.markdown('In this page, I will try to show you informations about our customers.')

    #Description of my dataset
    st.subheader('Dataset')
    st.markdown('In my dataset, I have 47 columns and 744 rows.')
    st.markdown('1 row represent 1 customer.')
    st.markdown('We have informations about their name, city of training, who training them, how much they are charged, etc.')
    st.write(my_data.head())



    #First plot
    st.subheader('Number of customers')
    st.markdown("This plot represents the number of customers by month :")
    chart_data = pd.DataFrame(my_data[["Cohorte","Customer"]].groupby(['Cohorte']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Cohorte':'index'}).set_index('index')
    st.line_chart(chart_data)


    #Image 3
    #Second plot
    st.subheader('Number of subscription to services')
    st.markdown("This second plot represents the number of customers who subscribe to the services :")
    chart_data = pd.DataFrame(my_data[["Adhésion","Customer"]].groupby(['Adhésion']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Adhésion':'index'}).set_index('index')
    st.bar_chart(chart_data)


    #Third plot
    st.subheader('Number of discontinue to services')
    st.markdown("This third plot represents the number of customers who discontinue to the services :")
    chart_data = pd.DataFrame(my_data[["Abandon","Customer"]].groupby(['Abandon']).sum().add_suffix('').reset_index())
    chart_data = chart_data.rename(columns={'Abandon':'index'}).set_index('index')
    st.bar_chart(chart_data)