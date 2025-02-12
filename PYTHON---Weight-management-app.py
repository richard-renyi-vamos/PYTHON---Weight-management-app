import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Load weight data (simulate a database with session state)
if 'weights' not in st.session_state:
    st.session_state.weights = []

st.title("🏋️ Weight Management App")

# Input for weight logging
today = datetime.date.today()
weight = st.number_input("Enter today's weight (kg):", min_value=30.0, max_value=200.0, step=0.1)
log_button = st.button("Log Weight")

if log_button:
    st.session_state.weights.append({"date": today, "weight": weight})
    st.success(f"Weight logged: {weight} kg on {today}")

# Display past records
if st.session_state.weights:
    df = pd.DataFrame(st.session_state.weights)
    st.write("### Weight Log")
    st.dataframe(df)
    
    # Plot weight trend
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['weight'], marker='o', linestyle='-')
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Weight Progress")
    st.pyplot(fig)

# Weight goal setting
goal_weight = st.number_input("Set your weight goal (kg):", min_value=30.0, max_value=200.0, step=0.1)
st.write(f"🎯 Your goal weight: {goal_weight} kg")
