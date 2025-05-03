import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Function to create a histogram
def histogram(data, column_name, title="Histogram"):
    fig, ax = plt.subplots()
    ax.hist(data[column_name], bins=10, edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel(column_name)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# Function to create a boxplot
def boxplot(data, column_name, title="Box Plot"):
    fig, ax = plt.subplots()
    sns.boxplot(y=data[column_name], ax=ax)
    ax.set_title(title)
    st.pyplot(fig)

# Function to create a scatter plot
def scatter_plot(data, x_column, y_column, title="Scatter Plot"):
    fig, ax = plt.subplots()
    ax.scatter(data[x_column], data[y_column])
    ax.set_title(title)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)

def scatter_plot_3d(data, x_column, y_column, z_column, title="3D Scatter Plot"):
    st.subheader(title)

    fig = px.scatter_3d(
        data,
        x=x_column,
        y=y_column,
        z=z_column,
        color=z_column,
        opacity=0.7
    )

    fig.update_layout(title=title)
    st.plotly_chart(fig)

def show_graphs():
    st.header("Wine Data Visualisation")
    
    # Load wine data from Excel
    data = pd.read_excel('C:/Users/ferdi/Desktop/Sem proj/BI-MP2-Wine_group11/data/wines_cleaned.xlsx')
    
    # Show the first few rows to verify data
    st.write(data.head())

    if all(col in data.columns for col in ['alcohol', 'chlorides', 'quality']):
        scatter_plot_3d(data, 'alcohol', 'chlorides', 'quality', title="Alcohol vs Chlorides vs Quality")

    # Show a histogram for alcohol content
    if 'alcohol' in data.columns:
        histogram(data, 'alcohol', title="Alcohol Content Distribution")
    
    # Show a boxplot for wine quality
    if 'quality' in data.columns:
        boxplot(data, 'quality', title="Wine Quality Distribution")
    
    # Show a scatter plot for alcohol vs. type
    if 'alcohol' in data.columns and 'quality' in data.columns:
        scatter_plot(data, 'alcohol', 'quality', title="Alcohol vs Quality")

    
