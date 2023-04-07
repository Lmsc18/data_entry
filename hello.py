import streamlit as st
import pandas as pd


def intro():
    import pandas as pd
    import streamlit as st
    import io

    # buffer to use for excel writer
    buffer = io.BytesIO()

    df=pd.read_excel('test.xlsx')
    df=df.sort_values(by=['Class'])
    st.write("""
        # VIEW DATA
    """)
    st.dataframe(df)

def ent_data():
    import pandas as pd
    import streamlit as st
    import io

    # buffer to use for excel writer
    buffer = io.BytesIO()

    df=pd.read_excel('test.xlsx')

    st.write("""
        # ENTER DATA
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

    



def del_data():
    import pandas as pd
    import streamlit as st
    import io

    # buffer to use for excel writer
    buffer = io.BytesIO()

    df=pd.read_excel('test.xlsx')

    st.write("""
        # Simple Data Entry App!!
    """)
    
    r_no=st.number_input('Roll Number:',value=0,step=1)


    col1,col2=st.columns(2)
    with col1:
        if st.button("Delete record"):
            q=df[df['Roll No']==r_no].index
            df.drop(q,axis=0,inplace=True)
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


def search_data():
    import pandas as pd
    import streamlit as st
    import io

    # buffer to use for excel writer
    buffer = io.BytesIO()

    df=pd.read_excel('test.xlsx')

    st.write("""
        # SEARCH DATA
    """)
    col1,col2=st.columns(2)
    r_no=col1.number_input('Roll Number:',value=0,step=1)
    cls=col2.selectbox("Select class: ",[9,10,11,12])


    
    if st.button("Search"):
        q=df[(df['Roll No']==r_no)&(df['Class']==cls)]
        st.write(q)

    
page_names_to_funcs = {
    "—": intro,
    "DELETE RECORD": del_data,
    "ENTER DATA": ent_data,
    "SEARCH DATA": search_data,
}

demo_name = st.sidebar.selectbox("Choose an operation: ", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()