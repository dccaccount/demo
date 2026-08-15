import glob
import os

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Employee Data", layout="wide")
st.title("Employee Data")

search_path = os.path.join(r"C:\emp", "Sample-Employee-Data*")
files = glob.glob(search_path)

if not files:
    st.error("No employee file found in C:\\emp")
    st.stop()

file_path = files[0]
file_name = os.path.basename(file_path)

if file_path.lower().endswith((".xlsx", ".xls")):
    df = pd.read_excel(file_path)
elif file_path.lower().endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    st.error(f"Unsupported file type: {file_name}")
    st.stop()

st.subheader(f"Loaded file: {file_name}")
st.dataframe(df, use_container_width=True)
