import streamlit as st
from helpers.data_loader import load_data
from helpers.visualization import visualize_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("Data Visualization with Streamlit")

    # Load data
    data = load_data("data/sierraleone-bumbuna.csv")

    # Convert 'Timestamp' column to datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Sidebar for selecting timestamp range
    st.sidebar.title('Select Timestamp Range')

    if 'Timestamp' in data:
        min_timestamp = data['Timestamp'].min()
        max_timestamp = data['Timestamp'].max()
        start_date = st.sidebar.date_input("Start Date", min_value=min_timestamp, max_value=max_timestamp, value=min_timestamp)
        end_date = st.sidebar.date_input("End Date", min_value=min_timestamp, max_value=max_timestamp, value=max_timestamp)
        start_time = st.sidebar.time_input("Start Time", value=pd.Timestamp.min.time())
        end_time = st.sidebar.time_input("End Time", value=pd.Timestamp.max.time())
        start_timestamp = pd.to_datetime(str(start_date) + ' ' + str(start_time))
        end_timestamp = pd.to_datetime(str(end_date) + ' ' + str(end_time))

        # Filter data based on selected timestamp range
        filtered_data = data[(data['Timestamp'] >= start_timestamp) & (data['Timestamp'] <= end_timestamp)]

        # Display filtered data
        st.subheader(f'Data for Timestamp Range: {start_timestamp} to {end_timestamp}')
        st.write(filtered_data)

        # Visualize data
        visualize_data(filtered_data)
    else:
        st.error("No 'Timestamp' column found in the dataset.")

    # Sidebar for customization options
    st.sidebar.title('Customize Graph')

    # Dropdown to select columns for x and y axes
    x_column = st.sidebar.selectbox('Select X-axis:', data.columns)
    y_column = st.sidebar.selectbox('Select Y-axis:', data.columns)

    # Slider to adjust marker size
    marker_size = st.sidebar.slider('Marker Size:', min_value=1, max_value=10, value=5)

    # Plot the graph
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_column, y=y_column, s=marker_size, ax=ax)
    ax.set_title(f'{x_column} vs {y_column}')
    st.pyplot(fig)

if __name__ == '__main__':
    main()