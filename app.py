import streamlit as st
import pandas as pd
import sys
import os

# Ensure Python recognizes the 'utils' directory
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import helper functions
from utils.data_loader import load_data
from utils.eda_functions import generate_summary, plot_histograms, correlation_heatmap

# Streamlit app title
st.title("📊 Interactive EDA App")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Load data
        df = load_data(uploaded_file)

        # Display raw data
        st.subheader("📋 Raw Data (First 5 Rows)")
        st.dataframe(df.head())

        # Generate and display dataset summary
        st.subheader("📊 Dataset Summary")
        summary = generate_summary(df)
        st.json(summary)

        # Show histograms
        st.subheader("📊 Histogram of Numerical Features")
        plot_histograms(df)

        # Show correlation heatmap
        st.subheader("🔍 Correlation Heatmap")
        correlation_heatmap(df)

    except Exception as e:
        st.error(f"⚠️ An error occurred while processing the file: {e}")
else:
    st.warning("⚠️ Please upload a CSV file to proceed.")
