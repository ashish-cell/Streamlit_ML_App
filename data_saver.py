import pandas as pd

import xlsxwriter
import openpyxl

def save_csv(df, filename):
    """
    Save a Pandas DataFrame to a CSV file.
    
    Parameters:
        - df (Pandas DataFrame): the DataFrame to save
        - filename (str): the filename (including path) to save the file to
    """
    df.to_csv(filename, index=False)

def save_excel(df, filename, sheet_name='Sheet1'):
    """
    Save a Pandas DataFrame to an Excel file.
    
    Parameters:
        - df (Pandas DataFrame): the DataFrame to save
        - filename (str): the filename (including path) to save the file to
        - sheet_name (str): the name of the Excel sheet to create (default: 'Sheet1')
    """
    #writer = pd.ExcelWriter(filename, engine='openpyxl')
    df.to_excel(filename, sheet_name=sheet_name, index=False)
    #writer.save()

def save_pickle(df, filename):
    """
    Save a Pandas DataFrame to a pickle file.
    
    Parameters:
        - df (Pandas DataFrame): the DataFrame to save
        - filename (str): the filename (including path) to save the file to
    """
    df.to_pickle(filename)
