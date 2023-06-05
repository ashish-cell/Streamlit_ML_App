import streamlit as st
import pandas as pd
from data_saver import save_csv, save_excel, save_pickle

def data_saving_app():
    """
    Main function for the Streamlit app.
    """
    # Define the page title and layout
    st.set_page_config(page_title="Data Saving App", layout="wide")

    # Define the sidebar
    st.sidebar.title("Save Data")

    # Define the main content
    st.title("Data Saving App")
    st.write("Use this app to save your data to different file formats.")

    # Define the file format options
    file_formats = ["CSV", "Excel", "Pickle"]

    # Define the file path input
    file_path = st.text_input("File Path")

    # Define the file format input
    file_format = st.selectbox("File Format", file_formats)

    # Define the data input
    data = st.text_area("Data")

    # Convert the data input to a DataFrame
    try:
        df = pd.read_csv(data)
    except:
        df = pd.DataFrame()

    # Define the save button
    if st.button("Save"):
        # Check if the file path and file format are valid
        if file_path and file_format:
            if file_format == "CSV":
                save_csv(df, file_path)
            elif file_format == "Excel":
                save_excel(df, file_path)
            elif file_format == "Pickle":
                save_pickle(df, file_path)

            # Show a success message
            st.success(f"{file_format} file saved to {file_path}")
        else:
            # Show an error message
            st.error("Please provide a file path and file format.")
if __name__ == '__main__':
    data_saving_app()
