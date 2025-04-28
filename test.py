'''
        quetta = df_activity.filter(items=['Quetta', 'Pishin', 'Killa Abdullah', 'Chaman'])
        sibi= df_activity.filter(items=['Sibi', 'Kohlu', 'Dera Bugti', 'Ziarat', 'Harnai'])
        zhob= df_activity.filter(items=['Zhob', 'Sherani', 'Killa Saifullah'])
        loralai= df_activity.filter(items=['Loralai', 'Duki', 'Musakhel', 'Barkhan'])
        kalat= df_activity.filter(items=['Khuzdar', 'Kalat', 'Surab', 'Lasbela', 'Hub', 'Awaran', 'Mastung'])
        naseerabad= df_activity.filter(items=['Nasirabad', 'Jaffarabad', 'Usta Muhammad', 'Jhal Magsi', 'Sohbat Pur'])
        makran=df_activity.filter(items=['Kech', 'Gwadar', 'Panjgur'])
        rakhshan=df_activity.filter(items=['Chagai', 'Nushki', 'Kharan', 'Washuk'])

        #st.write(df_activity['Quetta', 'Ziarat'])
        #st.write(df_activity['Ziarat'])
        
        #newdf = df_activity.filter(items=["name", "age"])
        st.dataframe(quetta)
        st.dataframe(sibi)
        st.dataframe(zhob)
        st.dataframe(loralai)
        st.dataframe(kalat)
        st.dataframe(naseerabad)
        st.dataframe(makran)
        st.dataframe(rakhshan)
   
'''    
