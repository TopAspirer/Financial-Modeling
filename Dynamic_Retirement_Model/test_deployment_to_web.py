


import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# App Title
st.title("Retirement Financial Model")

# Sidebar for Inputs
st.sidebar.header("User Input Parameters")
age = st.sidebar.slider("Current Age", 20, 65, 30)
retirement_age = st.sidebar.slider("Retirement Age", age + 1, 80, 65)
current_savings = st.sidebar.number_input("Current Savings ($)", min_value=0.0, value=50000.0, step=1000.0)
annual_savings = st.sidebar.number_input("Annual Savings ($)", min_value=0.0, value=10000.0, step=500.0)
return_rate = st.sidebar.slider("Annual Return Rate (%)", 0.0, 15.0, 5.0) / 100
inflation_rate = st.sidebar.slider("Inflation Rate (%)", 0.0, 10.0, 2.5) / 100
desired_income = st.sidebar.number_input("Desired Annual Retirement Income ($)", min_value=0.0, value=40000.0, step=1000.0)

# Calculations
years_to_retirement = retirement_age - age
future_value_savings = current_savings * ((1 + return_rate) ** years_to_retirement) + \
    annual_savings * (((1 + return_rate) ** years_to_retirement - 1) / return_rate)

inflation_adjusted_income = desired_income * ((1 + inflation_rate) ** years_to_retirement)
sustainable_years = future_value_savings / inflation_adjusted_income if inflation_adjusted_income > 0 else 0

# Display Results
st.header("Results")
st.subheader("Savings at Retirement")
st.write(f"💰 **Estimated Retirement Savings**: ${future_value_savings:,.2f}")

st.subheader("Retirement Duration Estimate")
st.write(f"📆 **Sustainable Years**: {sustainable_years:.1f} years of ${inflation_adjusted_income:,.2f} annual income.")

# Visualization
st.subheader("Savings Growth Over Time")
years = np.arange(age, retirement_age + 1)
savings = [current_savings * ((1 + return_rate) ** (y - age)) + 
           annual_savings * (((1 + return_rate) ** (y - age) - 1) / return_rate) 
           for y in years]

# Use Plotly for Interactive Chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=savings, mode='lines+markers', name='Savings Over Time'))
fig.update_layout(title="Projected Savings Growth",
                  xaxis_title="Age",
                  yaxis_title="Savings ($)",
                  template="plotly_white")
st.plotly_chart(fig)

# Option to Export Data
if st.button("Export Data"):
    df = pd.DataFrame({'Age': years, 'Savings ($)': savings})
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name='savings_data.csv', mime='text/csv')

