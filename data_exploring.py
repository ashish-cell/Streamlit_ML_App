import streamlit as st
import pandas as pd
from data_explorer import data_exploration

# Load data
data = pd.read_csv("covid_data.csv")

# Create Streamlit app
def data_exploring_app():
    st.set_page_config(page_title="Data Exploration App")

    # Display the title
    st.title("Data Exploration App")

    # Call the data exploration function
    data_exploration(data)

if __name__ == "__main__":
    data_exploring_app()
