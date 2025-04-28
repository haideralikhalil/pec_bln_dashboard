import streamlit as st 
import pandas as pd
import plotly.express as px 
from st_social_media_links import SocialMediaIcons

st.set_page_config(page_title="General Elections 2018",
                   page_icon="images/icon.webp",
                layout="wide")
st.title("General Elections 2018")

@st.cache_data
def load_data():
    # The sheet must be published to the web
    sheet_url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit#gid=0"
    
    # Convert to CSV export URL
    csv_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    
    # Read into DataFrame
    df = pd.read_csv(csv_url)
    
    # Select only columns A:L (first 12 columns)
    df = df.iloc[:, :12]
    
    # Limit to 3429 rows
    df = df.head(3429)
    
    return df
df = load_data()

records = df.shape[0]
#df_list_candidates = df
#df_returned_candidates = df[(df['Valid_Votes'] != 0)]

with st.sidebar:
    filter_selection = st.radio(
            "",
            ["By District", "By Constituency"],
            key="visibility",
            horizontal=True,
        )
    
    if filter_selection == "By District":
        district_options = ["ALL"] + list(df['District'].unique()) 
        district = st.selectbox (
            "Select District",
            options =district_options ,
            index = 0
        )
        
        if district == "ALL":
                st.session_state['title'] = "Pakistan"
                df = load_data()
                df_returned_candidates = df[(df['Valid_Votes'] != 0)]
                df_list_candidates = df
        else:
            st.session_state['title'] = district
            df = df[df['District'] == district]
            df_returned_candidates = df[(df['Valid_Votes'] != 0) & (df['District'] == district)]
            df_list_candidates = df[df['District'] == district]    
        
    if filter_selection == "By Constituency":
        constituency_options= ['ALL'] + df['Constituency'].unique().tolist()

        constituency = st.selectbox (
            "Select Constituency",
            options =constituency_options ,
            index = 0
        ) 
        if constituency == "ALL":
            st.session_state['title']="Pakistan"
            df = load_data()
            df_returned_candidates = df[(df['Valid_Votes'] != 0)]
            df_list_candidates = df
        else:
            st.session_state['title'] = constituency
            df = df[df['Constituency'] == constituency]
            df_returned_candidates = df[(df['Valid_Votes'] != 0) & (df['Constituency'] == constituency)]
            df_list_candidates = df[df['Constituency'] == constituency]


#st.title(f":blue[Pakistan]")

tab_overall, tab_contesting, tab_successful, tab_party01, tab_party02, tab_about = st.tabs(
        ["Overall Summary",
         "Contesting Candidates",
         "Successful Candidates",
         "Party Position [By Votes]",
         "Party Position [By Seats]",
        "About"
        ])
'''
with tab_overall:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(f"Registered Voters")
        st.subheader(f":blue[{df['Total_Registered_Voters'].sum():,}]")
        st.subheader("Votes Cast")
        st.subheader(f":blue[{df['Total_Votes'].sum():,}]")
    with col2:
        st.subheader("Valid Votes")
        st.subheader(f":blue[{df['Valid_Votes'].sum():,}]")
        st.subheader("Rejected Votes")
        st.subheader(f":blue[{df['Rejected_Votes'].sum():,}]")
    with col3:
        st.subheader("Turnout")
        turnout = df['Total_Votes'].sum() / df['Total_Registered_Voters'].sum() * 100
        turnout = round(turnout, 2)
        st.subheader(f":blue[{turnout}%]")    

with tab_contesting:
    records = df_list_candidates.shape[0]
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"List of Candidates")
    with col2:
        st.subheader(f":blue[{records}]")
    st.dataframe(df_list_candidates[['Constituency',  'Description', 'Candidate', 'Party', 'Votes']])

with tab_successful:
    st.subheader("Successful Candidates")
    st.dataframe(df_returned_candidates[['Constituency', 'Description', 'Candidate', 'Party', 'Votes']])

with tab_party01:
    st.subheader("No. of votes obtained by each Party [Top 10]")
    df_party01 = df.groupby('Party')['Votes'].sum().reset_index()
    df_top10 = df_party01.sort_values(by='Votes', ascending=False).head(10)
    df_top10 = df_top10[df_top10['Party'].notnull()]
    df_top10 = df_top10[df_top10['Party'] != '']
    df_top10 = df_top10.reset_index(drop=True) 
    df_top10.index = df_top10.index + 1 
    widths = [50, 150, 200]
    
    fig = px.pie(
        df_top10, 
        values='Votes', 
        names='Party',            
        hole=0.3
    )
    
    fig.update_traces(
        textinfo='percent+value', 
        textfont_size=12, 
        marker=dict(line=dict(color='#000000', width=1)) 
        )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df_top10,  width=sum(widths))

with tab_party02:
    st.subheader("Seats won by each Party [Top 10]")
    df_party02 = df[df['Valid_Votes'] != 0]
    df_party02 = df_party02.groupby('Party')['Constituency'].count().reset_index()
    df_top10 = df_party02.sort_values(by='Constituency', ascending=False).head(10)
    df_top10 = df_top10[df_top10['Party'].notnull()]
    df_top10 = df_top10[df_top10['Party'] != '']
    df_top10 = df_top10.reset_index(drop=True) 
    df_top10.index = df_top10.index + 1 
    widths = [50, 150, 200]
    
    df_top10['Party'] = df_top10['Party'].str.strip() 
    fig = px.pie(
        df_top10, 
        values='Constituency', 
        names='Party',
        hole=0.3
        )

    fig.update_traces(
        textinfo='percent+value', 
        textfont_size=14, 
        marker=dict(line=dict(color='#000000', width=1)) 
        )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df_top10,  width=sum(widths))

with tab_about:
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
'''