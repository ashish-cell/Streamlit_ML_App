import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt
import seaborn as sns

def data_exploration(df):
    st.header("Data Exploration")

    # Display the first few rows of the dataset
    if st.checkbox("Preview DataFrame"):
        st.write(df.head())

    # Display basic statistics of the dataset
    if st.checkbox("View Summary Statistics"):
        st.write(df.describe())

    # Generate a report using pandas profiling
    if st.checkbox("Generate Report with Pandas Profiling"):
        profile = ProfileReport(df, explorative=True)
        st_profile_report(profile)

    # Display a correlation heatmap of the dataset
    if st.checkbox("View Correlation Heatmap"):
        #corr = df.corr()
        plt.fig = plt.figure(figsize=(12,10))
        plot = sns.heatmap(df.corr(), annot=True)
        st.pyplot(plot) # Display heatmap

