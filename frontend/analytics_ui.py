import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"


def analytics_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date",datetime(2024,8,1))
    with col2:
        end_date = st.date_input("Start Date", datetime(2024, 8, 15))

    if st.button("Get Analytics"):
        payload = {
            "start_date":start_date.strftime("%Y-%m-%d"),
            "end_date":end_date.strftime("%Y-%m-%d")
        }
        result = requests.post(f"{API_URL}/analytics/",json=payload)
        result = result.json()
        data = {
            "Category": list(result.keys()),
            "Total":[result[category]["total"] for category in result],
            "Percentage": [result[category]["percentage"] for category in result]
        }
        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage",ascending=False)

        st.title("Expense Breakdown by Category")

        st.bar_chart(data=df_sorted.set_index("Category")["Percentage"],width=0,height=0,use_container_width=True)

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
        pie_fig = px.pie(df_sorted, names='Category', values='Percentage',
                         title="Expense Distribution by Category",
                         color='Category',
                         color_discrete_sequence=px.colors.qualitative.Set3,
                         hole=0.3)  # Creates a donut chart, can be set to 0 for a regular pie chart

        # Customize Pie chart to show percentages inside the chart
        pie_fig.update_traces(textinfo='percent+label',
                              pull=[0.1, 0.1, 0.1, 0.1, 0.1])  # Adjust the "pull" for visual appeal

        # Display the Plotly pie chart
        st.plotly_chart(pie_fig, use_container_width=True)
        st.table(df_sorted)