#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 


# In[12]:


import seaborn as sns


# In[6]:


import matplotlib.pyplot as plt


# In[49]:


data1=pd.read_csv("sierraleone-bumbuna.csv")


# In[50]:


data1.head()


# In[51]:


data1.shape


# In[52]:


# Convert 'timestamp' column to datetime if it's not already in datetime format
data1['Timestamp'] = pd.to_datetime(data1['Timestamp'])

# Plot GHI vs. Timestamp
data1.plot(x='Timestamp', y='GHI', kind='line', color='blue',linestyle='-')

plt.title('GHI vs. Time Stamp')
plt.xlabel('Time Stamp')
plt.ylabel('Global Horizontal Irradiance (GHI)')
plt.show()


# In[53]:



# Assuming 'data1' is your data1Frame containing the solar data1
# If your data1Frame is loaded from a CSV file, replace 'solar_data1.csv' with the actual file name

# Load the data1 into a data1Frame

# Select the columns 'DHI', 'GHI', and 'DNI' for correlation analysis
selected_columns = ['DHI', 'GHI', 'DNI']
correlation_matrix = data1[selected_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation coefficient')
plt.title('Correlation Matrix: DHI, GHI, and DNI')
plt.xticks(range(len(selected_columns)), selected_columns)
plt.yticks(range(len(selected_columns)), selected_columns)
plt.tight_layout()
plt.show()


# In[54]:


# Assuming 'data1' is your data1Frame containing the solar data1
# If your data1Frame is loaded from a CSV file, replace 'solar_data1.csv' with the actual file name

# Load the data1 into a data1Frame

# Plot WS, WSgust, and WSstdev on one plot
plt.figure(figsize=(10, 6))
plt.plot(data1['Timestamp'], data1['WS'], label='WS', color='blue', linestyle='-')
plt.plot(data1['Timestamp'], data1['WSgust'], label='WSgust', color='red', linestyle='-')
plt.plot(data1['Timestamp'], data1['WSstdev'], label='WSstdev', color='green', linestyle='-')

plt.title('Wind Speed, Gust, and Standard Deviation')
plt.xlabel('Timestamp')
plt.ylabel('Wind Speed (m/s)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


# In[55]:



# Create histograms for GHI, DNI, DHI, and WS
plt.figure(figsize=(12, 8))

# GHI histogram
plt.subplot(2, 2, 1)
plt.hist(data1['GHI'], bins=20, color='skyblue', edgecolor='black')
plt.title('Global Horizontal Irradiance (GHI) Histogram')
plt.xlabel('GHI')
plt.ylabel('Frequency')

# DNI histogram
plt.subplot(2, 2, 2)
plt.hist(data1['DNI'], bins=20, color='salmon', edgecolor='black')
plt.title('Direct Normal Irradiance (DNI) Histogram')
plt.xlabel('DNI')
plt.ylabel('Frequency')

# DHI histogram
plt.subplot(2, 2, 3)
plt.hist(data1['DHI'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Diffuse Horizontal Irradiance (DHI) Histogram')
plt.xlabel('DHI')
plt.ylabel('Frequency')

# WS histogram
plt.subplot(2, 2, 4)
plt.hist(data1['WS'], bins=20, color='orange', edgecolor='black')
plt.title('Wind Speed (WS) Histogram')
plt.xlabel('WS')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# In[72]:


from scipy.stats import skew, kurtosis

# Load your dataset (replace 'your_dataset.csv' with the actual filename)
data=pd.read_csv("sierraleone-bumbuna.csv")

# Summary statistics
summary_stats = data.describe()

# Calculate skewness
skewness = data.skew()

# Calculate kurtosis
kurtosis_val = data.kurtosis()

# Calculate interquartile range (IQR)
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

# Create a DataFrame to store the results
analysis_results = pd.DataFrame({
    'Mean': summary_stats.loc['mean'],
    'Median': data.median(),
    'Standard Deviation': summary_stats.loc['std'],
    'Skewness': skewness,
    'Kurtosis': kurtosis_val,
    'IQR': IQR
})

# Display the analysis results
print("Analysis Results:")
print(analysis_results)


# In[70]:


# Calculate correlation matrix
correlation_matrix = data1.corr()

# Display correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)


# In[59]:


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[14]:


# Drop the 'Comments' column
data1.drop(columns=['Comments'], inplace=True)

# Check the columns again to confirm that 'Comments' has been removed
print("Columns after removing 'Comments':", data1.columns)


# In[15]:


data1.head()


# In[17]:


data2=pd.read_csv("benin-malanville.csv")


# In[18]:


data2.head()


# In[20]:


data2.shape


# In[21]:


null_values = data2.isnull().sum()

# Display the count of null values for each column
print("Null values per column:")
print(null_values)


# In[23]:


# Convert 'timestamp' column to datetime if it's not already in datetime format
data2['Timestamp'] = pd.to_datetime(data2['Timestamp'])

# Plot GHI vs. Timestamp
data2.plot(x='Timestamp', y='GHI', kind='line', color='green',linestyle='-')
plt.title('GHI vs. Time Stamp')
plt.xlabel('Time Stamp')
plt.ylabel('Global Horizontal Irradiance (GHI)')
plt.show()


# In[24]:


# Assuming 'data2' is your data2Frame containing the solar data2
# If your data2Frame is loaded from a CSV file, replace 'solar_data2.csv' with the actual file name

# Load the data2 into a data2Frame

# Select the columns 'DHI', 'GHI', and 'DNI' for correlation analysis
selected_columns = ['DHI', 'GHI', 'DNI']
correlation_matrix = data2[selected_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation coefficient')
plt.title('Correlation Matrix: DHI, GHI, and DNI')
plt.xticks(range(len(selected_columns)), selected_columns)
plt.yticks(range(len(selected_columns)), selected_columns)
plt.tight_layout()
plt.show()


# In[25]:


# Assuming 'data2' is your data2Frame containing the solar data2
# If your data2Frame is loaded from a CSV file, replace 'solar_data2.csv' with the actual file name

# Load the data2 into a data2Frame

# Plot WS, WSgust, and WSstdev on one plot
plt.figure(figsize=(10, 6))
plt.plot(data2['Timestamp'], data2['WS'], label='WS', color='blue', linestyle='-')
plt.plot(data2['Timestamp'], data2['WSgust'], label='WSgust', color='red', linestyle='-')
plt.plot(data2['Timestamp'], data2['WSstdev'], label='WSstdev', color='green', linestyle='-')

plt.title('Wind Speed, Gust, and Standard Deviation')
plt.xlabel('Timestamp')
plt.ylabel('Wind Speed (m/s)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


# Create histograms for GHI, DNI, DHI, and WS
plt.figure(figsize=(14, 10))  # Increase figure size

# GHI histogram
plt.subplot(2, 2, 1)
plt.hist(data2['GHI'], bins=30, color='royalblue', edgecolor='black', alpha=0.8)  # Change color, bins, and transparency
plt.title('GHI Distribution', fontsize=16, color='navy', fontweight='bold')  # Change title font settings
plt.xlabel('Global Horizontal Irradiance (GHI)', fontsize=14, color='navy')  # Change x-axis label font settings
plt.ylabel('Frequency', fontsize=14, color='navy')  # Change y-axis label font settings

# DNI histogram
plt.subplot(2, 2, 2)
plt.hist(data2['DNI'], bins=30, color='darkred', edgecolor='black', alpha=0.8)  # Change color, bins, and transparency
plt.title('DNI Distribution', fontsize=16, color='darkred', fontweight='bold')  # Change title font settings
plt.xlabel('Direct Normal Irradiance (DNI)', fontsize=14, color='darkred')  # Change x-axis label font settings
plt.ylabel('Frequency', fontsize=14, color='darkred')  # Change y-axis label font settings

# DHI histogram
plt.subplot(2, 2, 3)
plt.hist(data2['DHI'], bins=30, color='darkgreen', edgecolor='black', alpha=0.8)  # Change color, bins, and transparency
plt.title('DHI Distribution', fontsize=16, color='darkgreen', fontweight='bold')  # Change title font settings
plt.xlabel('Diffuse Horizontal Irradiance (DHI)', fontsize=14, color='darkgreen')  # Change x-axis label font settings
plt.ylabel('Frequency', fontsize=14, color='darkgreen')  # Change y-axis label font settings

# WS histogram
plt.subplot(2, 2, 4)
plt.hist(data2['WS'], bins=30, color='darkorange', edgecolor='black', alpha=0.8)  # Change color, bins, and transparency
plt.title('WS Distribution', fontsize=16, color='darkorange', fontweight='bold')  # Change title font settings
plt.xlabel('Wind Speed (WS)', fontsize=14, color='darkorange')  # Change x-axis label font settings
plt.ylabel('Frequency', fontsize=14, color='darkorange')  # Change y-axis label font settings

plt.tight_layout()
plt.show()



