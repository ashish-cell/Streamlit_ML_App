import streamlit as st
from radiant_mlhub import Dataset
import pandas as pd

# Load a sample dataset from Radiant
dataset = Dataset.fetch("mlb-game-log")

# Convert the dataset to a Pandas dataframe
df = pd.DataFrame(dataset.data)

# Display the dataset in Streamlit
st.write(df)
