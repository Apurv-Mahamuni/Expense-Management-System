import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

def analytics_month_tab():
    results = requests.get(f"{API_URL}/month")
    if results.status_code == 200:
        results = results.json()
    df = pd.DataFrame(results)
    st.title("Expense Breakdown by Months")
    st.bar_chart(data=df.set_index("month_name")['Total'], use_container_width=True)
    df["Total"] = df["Total"].map("{:.2f}".format)
    st.table(df)