import pandas as pd
import streamlit as st
import io

# buffer to use for excel writer
buffer = io.BytesIO()

df=pd.read_excel('test.xlsx')

st.write("""
    # Simple Data Entry App!!
""")

col1, col2 = st.columns(2)

r_no=col1.number_input('Roll Number:',value=0,step=1)

name= col2.text_input('Name: ','Enter name')

cls=col1.selectbox("Select class: ",[9,10,11,12])

col1,col2=st.columns(2)
with col1:
    if st.button("ADD"):
        new=pd.Series([r_no,name,cls],index=df.columns)
        df=df.append(new,ignore_index=True)
        df.to_excel('test.xlsx',index=False)
        st.write(df)

with col2:
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        # Write each dataframe to a different worksheet.
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        # Close the Pandas Excel writer and output the Excel file to the buffer
        writer.save()

        download2 = st.download_button(
            label="Download data as Excel",
            data=buffer,
            file_name='out.xlsx',
            mime='application/vnd.ms-excel'
        )

st.markdown(
    """
    -[Delete Record](./delete.py)
    """
)


