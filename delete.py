import pandas as pd
import streamlit as st


df=pd.read_excel('test.xlsx')

st.write("""
    # Simple Data Entry App!!
""")

r_no=col1.number_input('Roll Number:',value=0,step=1)

if st.button("Delete record"):
    q=df[df['Roll No']==1].index
    df.drop(q,axis=0,inplace=True)
    df.to_excel('test.xlsx',index=False)
    st.write(df)