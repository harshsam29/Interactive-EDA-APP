import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def generate_summary(df):
    """
    Generates a basic dataset summary.
    
    Parameters:
    df (DataFrame): The input Pandas DataFrame.

    Returns:
    dict: A dictionary containing dataset summary information.
    """
    summary = {
        "Total Rows": df.shape[0],
        "Total Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum(),
        "Data Types": df.dtypes.to_dict(),
    }
    return summary

def plot_histograms(df):
    """
    Plots histograms for all numerical columns.
    
    Parameters:
    df (DataFrame): The input Pandas DataFrame.
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    df[numerical_cols].hist(figsize=(12, 6), bins=20, edgecolor="black")
    plt.tight_layout()
    st.pyplot(plt)

def correlation_heatmap(df):
    """
    Plots a heatmap of feature correlations.
    
    Parameters:
    df (DataFrame): The input Pandas DataFrame.
    """
    numerical_cols = df.select_dtypes(include=['number']).columns
    corr_matrix = df[numerical_cols].corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    st.pyplot(plt)
