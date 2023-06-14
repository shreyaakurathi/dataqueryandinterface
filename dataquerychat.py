# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:36:29 2023

@author: shrey
"""

import streamlit as st
import pandas as pd 


dflist = {
    'Linkedin Messages': 'data\messages.csv',
    'Gpay Cashback': 'data\cashback.csv',
    'Gpay Group payments': 'data\group.csv'
}

def load_climate_data(df):
    data = pd.read_csv(dflist[df])
    return data

def filter_data(data, attributes, query_values):
    filtered_data = data.copy()
    for attribute, value in zip(attributes, query_values):
        filtered_data = filtered_data[filtered_data[attribute].astype(str).str.contains(value, case=False)]
    return filtered_data

st.title("Data Query Search Engine")


selected_df = st.selectbox("Select a dataframe", list(dflist.keys()))


data = load_climate_data(selected_df)

attributes = list(data.columns)

# Multi-select box to choose attributes to query
selected_attributes = st.multiselect("Select attributes to query", attributes)

# Text input boxes for query values
query_values = []
for attribute in selected_attributes:
    query_value = st.text_input(f"Enter value for {attribute}")
    query_values.append(query_value)

# Filter data based on selected attributes and query values
filtered_data = filter_data(data, selected_attributes, query_values)

if filtered_data.empty:
    st.warning("No matching results found.")
else:
    st.write(f"Filtered Data for {selected_df}")
    st.dataframe(filtered_data)

