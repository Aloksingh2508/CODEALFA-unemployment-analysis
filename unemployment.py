import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Data Loading and Preparation
def load_and_prepare_data(file_path_1, file_path_2):
    # Load the datasets
    df1 = pd.read_csv(file_path_1)
    df2 = pd.read_csv(file_path_2)

    # Clean column names (strip leading/trailing spaces)
    df1.columns = df1.columns.str.strip()
    df2.columns = df2.columns.str.strip()

    # Strip any leading/trailing spaces from the 'Date' column
    df1['Date'] = df1['Date'].str.strip()
    df2['Date'] = df2['Date'].str.strip()

    # Convert 'Date' columns to datetime format, with dayfirst=True
    df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True, errors='coerce')
    df2['Date'] = pd.to_datetime(df2['Date'], dayfirst=True, errors='coerce')

    # Combine both datasets
    combined_df = pd.concat([df1, df2], ignore_index=True)
    return combined_df

# Step 2: Data Segmentation (Pre-COVID and Post-COVID)
def segment_data_by_covid(df):
    # Define the split date as March 1, 2020
    pre_covid = df[df['Date'] < '2020-03-01']
    post_covid = df[df['Date'] >= '2020-03-01']
    return pre_covid, post_covid

# Step 3: Plotting Unemployment Trends
def plot_unemployment_trend(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'], label='Unemployment Rate (%)', color='blue', marker='o')

    # Highlight COVID period
    plt.axvline(x=pd.Timestamp('2020-03-01'), color='red', linestyle='--', label='COVID Start (March 2020)')

    # Enhance the plot
    plt.title('Unemployment Rate Trend in India (COVID-19 Impact)', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Unemployment Rate (%)', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to execute the analysis
def analyze_covid_impact(file_path_1, file_path_2):
    # Load and prepare data
    combined_df = load_and_prepare_data(file_path_1, file_path_2)

    # Segment the data into pre and post COVID
    pre_covid_data, post_covid_data = segment_data_by_covid(combined_df)

    # Plot the unemployment trend over time
    plot_unemployment_trend(combined_df)

# File paths (replace with your actual file paths)
file_path_1 = r'C:\Users\Mr.Alok\Desktop\code alfa\unemp1.csv'
file_path_2 = r'C:\Users\Mr.Alok\Desktop\code alfa\unemp2.csv'

# Run the analysis
analyze_covid_impact(file_path_1, file_path_2)