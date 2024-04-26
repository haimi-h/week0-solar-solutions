import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(data):
    # Create a Matplotlib figure object
    fig, ax = plt.subplots()

    # Plot your data using Matplotlib or Seaborn
    # Example:
    sns.scatterplot(data=data, x='GHI', y='DNI', ax=ax)

    # Customize the plot as needed

    # Show the plot
    st.pyplot(fig)
