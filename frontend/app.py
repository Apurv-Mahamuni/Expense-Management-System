import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_month import analytics_month_tab
st.title("Expense Management System")

API_URL = "http://localhost:8000"

tab1,tab2,tab3 = st.tabs(["ADD/UPDATE","ANALYTICS BY CATEGORY","ANALYTICS BY MONTH"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_month_tab()