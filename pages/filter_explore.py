import streamlit as st
import pandas as pd
st.set_page_config(page_title="Smart Filtering", layout="wide")
st.title("Smart, Intuitive Data Filtering")

from streamlit_dynamic_filters import DynamicFilters

if "data" not in st.session_state:
    st.warning("Go to Data Preview, upload a file, then return here.")
else:
    data = st.session_state["data"]
    show_cols = st.multiselect("Columns to filter:", list(data.columns), default=list(data.columns))
    dynamic_filters = DynamicFilters(data, filters=show_cols)
    dynamic_filters.display_filters(location='columns', num_columns=2)
    filtered_df = dynamic_filters.filter_df() if hasattr(dynamic_filters, "filter_df") else dynamic_filters.display_df()
    st.write(f"Filtered Rows: {len(filtered_df)}")
    st.dataframe(filtered_df, use_container_width=True)
    st.button("Reset Filters", on_click=lambda: st.session_state.pop('filtered_df', None))

