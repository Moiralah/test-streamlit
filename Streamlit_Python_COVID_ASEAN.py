import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the provided URL
url = "https://raw.githubusercontent.com/Moiralah/test-streamlit/main/owid-covid-data%20ASEAN%201.csv"
df = pd.read_csv(url)

# Set option to display float values with two decimal places
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Fill NaN values with 0
df.fillna(0, inplace=True)

# Create a Streamlit app title
st.title("COVID-19 ASEAN 2020-2022 Data Analysis")

# Sidebar for selecting locations
selected_location = st.sidebar.selectbox("Select a Location", df['location'].unique())

# Filter data based on selected location
filtered_df = df[df['location'] == selected_location]

# Create subplots for each metric
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Plot new cases
axes[0, 0].plot(filtered_df['date'], filtered_df['new_cases'])
axes[0, 0].set_title('New Cases')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Count')

# Plot new deaths
axes[0, 1].plot(filtered_df['date'], filtered_df['new_deaths'], color='red')
axes[0, 1].set_title('New Deaths')
axes[0, 1].set_xlabel('Date')
axes[0, 1].set_ylabel('Count')

# Plot new vaccinations
axes[1, 0].plot(filtered_df['date'], filtered_df['new_vaccinations'], color='green')
axes[1, 0].set_title('New Vaccinations')
axes[1, 0].set_xlabel('Date')
axes[1, 0].set_ylabel('Count')

# Plot stringency index
axes[1, 1].plot(filtered_df['date'], filtered_df['stringency_index'], color='purple')
axes[1, 1].set_title('Stringency Index')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Index')

# Adjust layout
plt.tight_layout()

# Display plots
st.pyplot(fig)

# Show population density for the selected location
st.write(f"Population Density for {selected_location}: {filtered_df['population_density'].iloc[0]}")

# Display data table for the selected location
st.write("Data for the selected location:")
st.write(filtered_df)
