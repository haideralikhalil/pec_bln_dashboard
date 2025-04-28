import streamlit as st 
import pandas as pd
import plotly.express as px 
import gdown
from PIL import Image
from io import BytesIO

@st.cache_data
def load_data():
    
    sheet_id = "1GVqvDQV42mQEirI325dTBreq7T7rdJO_kKveHPrN1dQ"
    sheet_name = "RECs"  # The name of your target sheet
    # Construct the URL
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    
    # Read into DataFrame
    df_RECs = pd.read_csv(csv_url)
    # Select only columns A:L (first 12 columns)
    df_RECs = df_RECs.iloc[:, :12]
    # Limit to 3429 rows
    df_RECs = df_RECs.head(3429)
    
    # DECs
    sheet_name = "DECs"  # The name of your target sheet
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df_DECs = pd.read_csv(csv_url)
    df_DECs = df_DECs.iloc[:, :12]
    df_DECs = df_DECs.head(3429)

    # HQ
    sheet_name = "HQ"  # The name of your target sheet
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df_HQ = pd.read_csv(csv_url)
    df_HQ = df_HQ.iloc[:, :12]
    df_HQ = df_HQ.head(3429)

    # Activities
    sheet_name = "Activities"  # The name of your target sheet
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df_activities = pd.read_csv(csv_url)
    df_activities = df_activities.iloc[:, :42]
    df_activities = df_activities.head(3429)

    # Constituencies
    sheet_name = "Constituencies"  # The name of your target sheet
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df_constituencies = pd.read_csv(csv_url)
    df_constituencies = df_constituencies.iloc[:, :42]
    df_constituencies = df_constituencies.head(3429)


    return df_RECs, df_DECs, df_HQ, df_activities, df_constituencies

def display_with_gdown(url, width=None):
    try:
        file_id = url.split('/d/')[1].split('/')[0]
        direct_url = f"https://drive.google.com/uc?id={file_id}"
        
        # Download to memory
        output = BytesIO()
        gdown.download(direct_url, output, quiet=True)
        img = Image.open(output)
        
        st.image(img, width=width)
    except Exception as e:
        #st.error(f"Error: {str(e)}")
        st.write("")


def call_phone(phone_number):
    # Method 1: Using markdown with HTML
    st.markdown(f"""
    <a href="tel:{phone_number}">
        <button style="background-color: #25D366; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px;">
            Call Us: {phone_number}
        </button>
    </a>
    """, unsafe_allow_html=True)