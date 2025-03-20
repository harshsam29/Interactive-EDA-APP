import pandas as pd

def load_data(uploaded_file):
    """
    Loads dataset from a CSV file into a Pandas DataFrame.
    
    Parameters:
    uploaded_file (file): A file object uploaded through Streamlit.

    Returns:
    DataFrame: Pandas DataFrame containing the dataset.
    """
    df = pd.read_csv(uploaded_file)
    return df
