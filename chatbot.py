# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:59:43 2023

@author: shrey
"""
import streamlit as st
import pandas as pd
from streamlit_chat import message

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)

def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']


def on_option(response):
        if response== '1':
            df = pd.read_csv("data\messages.csv")
            st.write("Linkedin Messages Dataset:")
            st.write("There are", len(df), "entries")
            st.dataframe(df)
        elif response =='2':
            df = pd.read_csv("data\cashback.csv")
            st.write("Gpay Cashbacks:")
            st.write("There are", len(df), "entries")
            st.dataframe(df)
        elif response =='3':
            df = pd.read_csv("data\group.csv")
            st.write("Gpay Group transactions:")
            st.write("There are", len(df), "entries")
            st.dataframe(df)
        else:
            message("enter a valid number")
            
def filter_data(data, attributes, query_values):
    filtered_data = data.copy()
    for attribute, value in zip(attributes, query_values):
        filtered_data = filtered_data[filtered_data[attribute].astype(str).str.contains(value, case=False)]
    return filtered_data

              

def quer(response):
    if response == "y":
        message("Awesome")
    else:
        message("SEE YOU SOON")
        exit()

        
def attr(response):
    dataset_choice = st.session_state.responses[0]
    if dataset_choice == '1':
            dataset = pd.read_csv("data\messages.csv")
    elif dataset_choice == '2':
        dataset = pd.read_csv("data\cashback.csv")
    elif dataset_choice == '3':
        dataset = pd.read_csv("data\group.csv")
    else:
        message("Invalid dataset choice")
        return
    filtered_data = dataset[response]
    st.write("Filtered Data:")
    st.write("There are", len(filtered_data), "entries")
    st.dataframe(filtered_data)

def value(response):
    dataset_choice = st.session_state.responses[0]
    col_choice = st.session_state.responses[2]
    if dataset_choice == '1':
            dataset = pd.read_csv("data\messages.csv")
    elif dataset_choice == '2':
        dataset = pd.read_csv("data\cashback.csv")
    elif dataset_choice == '3':
        dataset = pd.read_csv("data\group.csv")
    else:
        message("Invalid dataset choice")
        return
    filtered_data = dataset[dataset[col_choice].astype(str).str.contains(response, case=False)]
    st.write("Filtered Data:")
    st.write("There are", len(filtered_data), "entries")
    st.dataframe(filtered_data)
    
        

st.session_state.setdefault('questions', [])

st.title("Data Querying chatbot!")
questions_list = ['Choose a dataset to get started!\n 1: Linkedin Messages\n 2: Gpay Cashbacks\n 3: Gpay Group Transactions ', 
                  'Do you want to query?',
                 'Enter attribute','What value do you want to query it by?','Great working with you today,bye!']


if 'responses' not in st.session_state.keys():
    st.session_state.questions.extend(questions_list)
    st.session_state.responses = []

chat_placeholder = st.empty()
st.button("Clear message", on_click=on_btn_click)

message(st.session_state.questions[0]) 

with st.container():
    functions = [on_option,quer,attr,value]
    for response, question,function in zip(st.session_state.responses, st.session_state.questions[1:], functions):
        message(response, is_user = True)
        function(response)
        message(question)

with st.container():
    st.text_input("User Response:", on_change=on_input_change, key="user_input")