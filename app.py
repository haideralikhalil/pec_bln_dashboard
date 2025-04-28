import streamlit as st 
import pandas as pd
import plotly.express as px 
from st_social_media_links import SocialMediaIcons
import base64
from io import BytesIO
from PIL import Image
import gdown
import data_funcs
import gspread
from google.oauth2.service_account import Credentials
import phone_call

st.set_page_config(page_title="PEC Balochistan Dashboard",
                   page_icon="images/icon.webp",
                layout="wide")


#phone_call.call_phone("+923219032716")

df_RECs, df_DECs, df_HQ, df_activities, df_constituencies = data_funcs.load_data()

tab_home,  tab_activities, tab_offices, tab_RECs,  tab_HQ, tab_const, tab_about,  = st.tabs(
        ["Home", "Activities","DECs","RECs","HQ Officers","Constituencies","About"])

with tab_home:
    st.title("PEC Balochistan Dashboard")
    col1, col2, col3= st.columns(3)
    with col1:
        st.write("**Field Offices**")   
        st.metric(label="Regional Election Commissioners", value=8,  border=True)
        st.metric(label="District Election Commissioners", value=36,  border=True)
        
    with col2:
        st.write("**Registered Voters**")   
        st.metric(label="Total", value=f"{5566441:,}",  border=True)
        st.metric(label=":mens: Male", value=f"{3117944:,}",  border=True)
        st.metric(label=":womens: Female", value=f"{2448497:,}",  border=True)
 
    with col3:
        st.write("**Constituencies**")
        st.metric(label="National Assembly", value=16,  border=True)
        st.metric(label="Provincial Assembly", value=52,  border=True)
        
           
with tab_const:
    st.subheader("List of Constituencies")
    st.dataframe(df_constituencies)
        
    
with tab_RECs:
    #st.dataframe(df_RECs)
    selected_rec = st.selectbox("REC",options=["ALL"] + df_RECs['Name'].unique().tolist(),index=0)
    
    if selected_rec=="ALL":
        st.subheader("Regional Elections Commissioners")
        st.dataframe(df_RECs) 
    else:
        df_rec = df_RECs[df_RECs['Name'] == selected_rec]
    
        col2, col3 = st.columns(2)
    
        with col2:
            st.header(selected_rec)
            df_rec['Landline No'] = df_rec['Landline No'].astype('Int64') 
            st.write(":phone:", df_rec['Landline No'].values[0])
            st.write(":iphone:",  df_rec['Cell No'].values[0])
            st.write(":email: " , df_rec['Email'].values[0])
            st.write(":house_buildings:", df_rec['Address'].values[0])
        with col3:
            if df_rec['Photo'].values[0]:
                data_funcs.display_with_gdown(df_rec['Photo'].values[0], width=200)
        #st.dataframe(df_rec)
    
with tab_HQ:
    st.subheader("PEC HQ Officers")
    selected_officer = st.selectbox("Officers",options=["ALL"] + df_HQ['Name'].unique().tolist(),index=0)
    
    if selected_officer=="ALL":
        st.subheader("HQ Officers")
        st.dataframe(df_HQ[['Name','Designation','Landline No','Cell No', 'Email']]) 
    else:
        df_HQ = df_HQ[df_HQ['Name'] == selected_officer]
        
        col1, col2 = st.columns([1, 3])
        with col1:
            
            st.subheader(df_HQ['Name'].values[0])
            st.subheader(df_HQ['Designation'].values[0])
            st.write(":phone:", df_HQ['Landline No'].values[0])
            st.write(":iphone:",  df_HQ['Cell No'].values[0])
            st.write(":email: " , df_HQ['Email'].values[0])
        with col2:
            if df_HQ['Photo'].values[0]:
                data_funcs.display_with_gdown(df_HQ['Photo'].values[0], width=400)

with tab_offices:
    selected_dec = st.selectbox("DECs",options=["ALL"] + df_DECs['District'].unique().tolist(),index=0)
    
    if selected_dec=="ALL":
        st.subheader("Districts and DECs")
        st.dataframe(df_DECs) 
    else:
        df_dec = df_DECs[df_DECs['District'] == selected_dec]
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader(df_dec['District'].values[0])
            st.subheader(df_dec['Name'].values[0])
            
            st.write(":phone:", df_dec['Landline No'].values[0])
            st.write(":iphone:", df_dec['Cell No'].values[0])
            st.write(":email: " , df_dec['Email'].values[0])
            st.write(":house_buildings:", df_dec['Address'].values[0])
            if df_dec['Photo'].values[0]:
                data_funcs.display_with_gdown(df_dec['Photo'].values[0], width=200)

        with col2:
            st.dataframe(df_activities[['Activity', 'Start Date', 'End Date', 'Status', selected_dec]])   
     
with tab_activities:
    
    selected_activity = st.selectbox("Activity",options=["ALL"] + df_activities['Activity'].unique().tolist(),index=0)
    
    if selected_activity=="ALL":
        st.subheader("Activities")
        st.dataframe(df_activities.sort_values('Start Date', ascending=False)) 
    else:
        df_activity = df_activities[df_activities['Activity'] == selected_activity]
        st.dataframe(df_activity[['Start Date','End Date', 'Status']])

        received=awaited=0
        rec_str=awaited_str=""
        col_no=0
        for col in df_activity.columns:
            col_no +=1
            if col_no<6:
                continue
            if (df_activity[col].astype(str).str.contains("Received")).any():
                received +=1
                rec_str = rec_str + col + ", " 
            else:
                awaited +=1
                awaited_str = awaited_str + col + ", "
        
        option_map = {
            "Received": f":ballot_box_with_check: Received [{received}]",
            "Awaited": f":watch: Awaited [{awaited}]",
            
        }
        status = st.segmented_control(
            None,
            options=option_map.keys(),
            format_func=lambda option: option_map[option],
            selection_mode="single",
        )
        #st.write("Status: ", status)
        if status=="Received":
            st.write(rec_str)    
        if status=="Awaited":
            st.write(awaited_str)    

with tab_about:
    #st.snow()
    st.subheader("Developed By Haider Ali")
    st.write("A Python Developer")
    
    social_media_links = [
        "https://www.linkedin.com/in/haiderkhalil",
        "https://www.medium.com/@haiderkhalil",
        "https://www.x.com/haiderhalil",
        "https://www.facebook.com/haideralikhalil",
        "https://www.youtube.com/@towncoder",
        "https://www.github.com/haideralikhalil",
        "https://wa.me/00923219032716"
    ]
    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()  
    st.divider()
    st.video("https://youtu.be/ZlLtP16jIM4") 

