import pandas as pd
import requests
import io

def read_csv(file_path):
    """
    This function reads data from a CSV file and returns a Pandas DataFrame.
    
    Parameters:
    -----------
    file_path: str
        File path of the CSV file to be read
        
    Returns:
    --------
    Pandas DataFrame
    """
    df = pd.read_csv(file_path)
    return df



def read_excel(file_path, sheet_name):
    """
    This function reads data from an Excel file and returns a Pandas DataFrame.
    
    Parameters:
    -----------
    file_path: str
        File path of the Excel file to be read
    sheet_name: str
        Sheet name from which the data is to be read
        
    Returns:
    --------
    Pandas DataFrame
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df


def read_url(url):
    """
    This function reads data from a URL and returns a Pandas DataFrame.
    
    Parameters:
    -----------
    url: str
        URL from which the data is to be read
        
    Returns:
    --------
    Pandas DataFrame
    """
    response = requests.get(url)
    data = response.text
    df = pd.read_csv(io.StringIO(data))
    return df



