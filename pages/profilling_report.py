import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import os

st.set_page_config(page_title="EDA Profiling", layout="wide")
st.title("Automated EDA Profiling")

uploaded_file = st.file_uploader("Upload file", type=["csv", "xlsx"])
df = None
if uploaded_file:
    # Support both CSV and Excel uploads
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        sheets = pd.ExcelFile(uploaded_file).sheet_names
        sheet = st.selectbox("Choose Excel sheet:", sheets)
        df = pd.read_excel(uploaded_file, sheet_name=sheet)

if df is not None:
    st.dataframe(df.head(10), use_container_width=True)
    if st.button("Create EDA Profiling Report"):
        with st.spinner("Generating profiling report..."):
            # Save to temp file to avoid collisions; use session or time-based name if desired
            report_filename = "_profile_report.html"
            profile = ProfileReport(df, title="Data Profile Report", minimal=True)
            profile.to_file(report_filename)
            with open(report_filename, "r", encoding="utf-8") as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
            st.download_button(
                label="Download EDA report (HTML)",
                data=html_content,
                file_name="profile_report.html",
                mime="text/html"
            )
else:
    st.info("Upload a CSV or Excel file to view profiling report.")
