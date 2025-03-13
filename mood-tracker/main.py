import streamlit as st  # for creating the web interface
import pandas as pd  # for data manipulation
import datetime  # for handling the dates
import csv  # for reading and writing the csv files
import os  # for file operations

MOOD_FILE = "mood_log.csv"

# Load mood data
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=['Date', 'Mood'])
    return pd.read_csv(MOOD_FILE)

# Save mood data
def save_mood_data(date, mood):
    # Check if the file exists before writing
    file_exists = os.path.exists(MOOD_FILE)
    with open(MOOD_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        # Write headers only if the file does not exist
        if not file_exists:
            writer.writerow(['Date', 'Mood'])
        writer.writerow([date, mood])

# Streamlit UI setup
st.title("Mood Tracker")

today = datetime.date.today()
st.subheader("How are you feeling today?")
mood = st.selectbox("Select your Mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully!")

# Load mood data for visualization
data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time")

    # Ensure the 'Date' column is available
    if 'Date' in data.columns:
        data["Date"] = pd.to_datetime(data['Date'])
        data.columns = data.columns.str.strip()  # Remove leading/trailing spaces from column names

        mood_counts = data.groupby("Mood").count()["Date"]
        st.bar_chart(mood_counts)
    else:
        st.subheader("Date column not found!")
