import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Preview", layout="wide")
st.title("Data Upload & Preview")

# File uploader widget: supports both CSV and Excel
uploaded_file = st.file_uploader("Upload Excel or CSV file", type=["csv", "xlsx"])
data = None
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            xls = pd.ExcelFile(uploaded_file)
            sheets = xls.sheet_names
            sheet = st.selectbox("Choose Excel sheet:", sheets)
            data = pd.read_excel(uploaded_file, sheet_name=sheet)
        st.session_state["data"] = data
        st.success("File uploaded! Previewing data below.")
        st.dataframe(data.head(20), use_container_width=True)
        st.write(f"Rows: {data.shape[0]} | Columns: {list(data.columns)}")
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Upload a CSV or Excel file above to preview and analyze.")
