import streamlit as st
import pandas as pd
import plotly.express as px
import kaleido
st.set_page_config(page_title="Custom Charts", layout="wide")
st.title("Custom Interactive Chart Builder")
if "data" not in st.session_state:
    st.warning("Upload and preview data first.")
else:
    df = st.session_state["data"]
    chart_type = st.selectbox("Chart type:", ["Bar", "Scatter", "Line", "Histogram", "Box", "Pie"])
    columns = df.select_dtypes(include=["number", "object", "category"]).columns.tolist()
    if len(columns) >= 2:
        x_col = st.selectbox("X Axis", columns)
        y_col = st.selectbox("Y Axis", columns, index=1)
        group_col = st.selectbox("Group By (optional)", [None] + columns)
        color = group_col if group_col else None
        if chart_type == "Bar":
            fig = px.bar(df, x=x_col, y=y_col, color=color, text_auto=True, barmode="group")
            fig.update_traces(textposition="outside")
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_col, y=y_col, color=color)
        elif chart_type == "Line":
            fig = px.line(df, x=x_col, y=y_col, color=color)
        elif chart_type == "Histogram":
            fig = px.histogram(df, x=x_col, color=color)
        elif chart_type == "Box":
            fig = px.box(df, x=x_col, y=y_col, color=color)
        elif chart_type == "Pie":
            fig = px.pie(df, names=x_col)
        st.plotly_chart(fig, use_container_width=True)
        st.download_button("Download Chart PNG", fig.to_image(format='png'), file_name="chart.png")
        st.download_button("Download Chart Data CSV", df.to_csv(index=False), file_name="chart_data.csv")
    else:
        st.error("Need at least two columns to plot.")
