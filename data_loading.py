import openpyxl
import os
import pandas as pd
import requests
import streamlit as st
from data_loader import read_csv, read_excel, read_url

def load_csv():
    # Use Streamlit's file uploader to prompt the user to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    # If a file has been uploaded
    if uploaded_file is not None:
        # Read the file into a Pandas DataFrame using read_csv
        df = read_csv(uploaded_file)
        # Return the DataFrame
        return df

def load_excel():
    # Use Streamlit's file uploader to prompt the user to upload an Excel file
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
    # If a file has been uploaded
    if uploaded_file is not None:
        # Prompt the user to enter the name of the sheet they want to load
        sheet_name = st.text_input("Enter the name of the sheet to load")
        # Read the sheet into a Pandas DataFrame using read_excel
        df = read_excel(uploaded_file, sheet_name=sheet_name)
        # Return the DataFrame
        return df

def load_url():
    # Prompt the user to enter the URL for the data file
    url = st.text_input("Enter the URL for the data file")
    # If a URL has been entered
    if url != "":
        # Call the read_url function and return the resulting DataFrame
        df = read_url(url)
        # Return the DataFrame
        return df

def data_loading_app():
    # Display a menu to allow the user to select the type of data source
    data_source = st.selectbox("Select a data source:", ["CSV file", "Excel file", "URL"])
    # Call the appropriate load function based on the user's selection
    if data_source == "CSV file":
        df = load_csv()
    elif data_source == "Excel file":
        df = load_excel()
    elif data_source == "URL":
        df = load_url()
    else:
        df = None
    # Display the resulting DataFrame to the user
    if df is not None:
        st.dataframe(df)

if __name__ == '__main__':
    data_loading_app()
