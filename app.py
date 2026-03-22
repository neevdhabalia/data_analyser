import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dataset Analyzer App")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.dataframe(df)

    st.write("### Column Selection")
    column = st.selectbox("Choose a column", df.columns)

 #adding colums for histogram
   
    if df[column].dtype != 'object':
    	fig, ax = plt.subplots(figsize=(8,5))
    	ax.hist(df[column], bins=10, edgecolor='black')
    	ax.set_title(f"Distribution of {column}")
    	ax.set_xlabel(column)
    	ax.set_ylabel("Frequency")
    	st.pyplot(fig)
    else:
    	st.write("This column is not numeric, cannot plot histogram.")
    
#adding correlation and covariance
    

    st.write("### Correlation & Covariance")

    col1 = st.selectbox("Select first column", df.columns)
    col2 = st.selectbox("Select second column", df.columns)

# Only for numeric data
    if df[col1].dtype != 'object' and df[col2].dtype != 'object':
    
    	correlation = df[col1].corr(df[col2])
    	covariance = df[col1].cov(df[col2])

    	st.write(f"Correlation between {col1} and {col2}: ", correlation)
    	st.write(f"Covariance between {col1} and {col2}: ", covariance)

    else:
    	st.write("Please select numeric columns only.")
    
    
    st.write("### Scatter Plot")

    if df[col1].dtype != 'object' and df[col2].dtype != 'object':
        fig, ax = plt.subplots(figsize=(8,5))
    
        ax.scatter(df[col1], df[col2])
    
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        ax.set_title(f"{col1} vs {col2}")
    
        st.pyplot(fig)
    else:
        st.write("Scatter plot only for numeric columns.")
