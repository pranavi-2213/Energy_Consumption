import streamlit as st          # for creating interactive web dashboard
import pandas as pd             # for data manipulation and analysis
import numpy as np              # for numerical operations
import time                     # used for simulating real-time updates
import plotly.express as px     # For data visulalization, interactivity, real-time updates and Professional Presentation

# Page configuration for streamlit 

st.set_page_config(page_title="Energy Consumption Analytics", 
                   layout="wide")     # sets title and layout

# Display title and description
st.title("Energy Consumption Analytics Dashboard")
st.markdown("### Real-Time Analysis of PJM Hourly Energy Consumption Data")
st.markdown("---")


# Load data with caching to get better performance 
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\karna\Downloads\PJME_hourly.csv\PJME_hourly.csv")    # Load CSV data
    df.columns = ['Datetime', 'MW']                                                  # Rename columns for clarity
    df['Datetime']= pd.to_datetime(df['Datetime'])                                   # Convert string to datetime format
    df = df.sort_values('Datetime')                                                  # Sort date in ascending order for time series analysis

    # Extract useful time components for analysis
    df['year'] = df["Datetime"].dt.year                                              # Extract year
    df['month'] = df["Datetime"].dt.month                                            # Extract month
    df['day'] = df["Datetime"].dt.day                                                # Extract day
    df['hour'] = df["Datetime"].dt.hour                                              # Extract hour
    df['Dayofweek'] = df["Datetime"].dt.day_name()                                   # Extract day of week
    return df

df = load_data()                                                                    # Call the function to load data

# Simulate real-time data stream
st.sidebar.header("Controls")
refresh = st.sidebar.checkbox("simulate real-time updates", value = True)

# option to display only last N rows
if refresh:
    n = st.sidebar.slider("Show last N records", 100, 1000, 500)
    df_display = df.tail(n)

else:
    df_display = df                                                                 # Show full dataset


# Summary Metrics

st.subheader("Key Metrics")

# Divide layout into 4 columns for metrics

col1, col2, col3, col4 = st.columns(4)

# Max and Min
max_row = df.loc[df['MW'].idxmax()]
min_row = df.loc[df['MW'].idxmin()]

# Display metrics in respective columns

col1.metric("Max consumption (MW)", f"{max_row['MW']:.2f}")
col2.metric("max timestamp", str(max_row['Datetime']))

col3.metric("Min consumption (MW)", f"{min_row['MW']:.2f}")
col4.metric("min timestamp", str(min_row["Datetime"]))

st.markdown("---")

# Visualizations
st.subheader("Energy Consumption Over Time")
fig1 = px.line(df_display, x= 'Datetime', y = 'MW',
               title = "ENERGY CONSUMPTION TREND",
               labels={'Datetime':'Time', 'MW': 'Megawatts'},
               template="plotly_dark")

st.plotly_chart(fig1, use_container_width = True)


st.subheader("Average Consumption by Hour of Day")
hourly_avg = df.groupby('hour')['MW'].mean().reset_index()
fig2 = px.bar(hourly_avg, x='hour', y='MW', text_auto=True,
              color='MW', color_continuous_scale='Blues',
              title="Avg Energy Consumption per Hour")
st.plotly_chart(fig2, use_container_width=True)


col5, col6 = st.columns(2)

with col5:
    daily_avg = df.groupby(df['Datetime'].dt.date)['MW'].mean().reset_index()
    fig3 = px.line(daily_avg, x='Datetime', y='MW',
                   title = "Daily Avg consumption",
                   labels = {"Datetime": "Date", "MW":"Avg MW"},
                   template = "plotly_white")
    st.plotly_chart(fig3, use_container_width=True)

with col6:
    monthly_avg = df.groupby('month')['MW'].mean().reset_index()
    fig4 = px.bar(monthly_avg, x='month', y='MW', text_auto=True,
                  title="Monthly Avg consumption",
                  labels={'month':'month', 'MW':'Avg MW'},
                  color = 'MW',
                  color_continuous_scale = 'Tealgrn')
    st.plotly_chart(fig4, use_container_width=True)


st.markdown("---")


# Detailed Min Consumption Information
st.subheader("minimum Consumption details")

min_details = {
    "minimum MW value": f"{min_row['MW']:.2f}",
    "Year": min_row['Datetime'].year,
    "Month": min_row['Datetime'].month,
    "Date": str(min_row['Datetime'].date()),
    "Hour":f"{min_row['Datetime'].hour}:00",
    "Exact Timestamp": str(min_row['Datetime'])
}

st.json(min_details)

st.subheader("Energy Usage Around Minimum Point")
window_df = df[(df['Datetime'] >= min_row['Datetime'] - pd.Timedelta(hours=24)) &
               (df['Datetime'] <= min_row['Datetime'] + pd.Timedelta(hours=24))]
fig5 = px.line(window_df, x='Datetime', y='MW',
               title="Energy Consumption 24 Hours Before and After Minimum Point",
               labels={'Datetime':'Time', 'MW':'Megawatts'},
               template="plotly_dark")  
fig5.add_vline(x=min_row['Datetime'], line_dash="dash", line_color="red")
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.markdown("Developed by Pranavi Karnam | Data Analytics Enthusiast")