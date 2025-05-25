# import streamlit as st
# import pandas as pd
# from io import BytesIO 

# st.set_page_config(page_title="📁File-Converter & Cleaners", layout="wide")
# st.title("📁File-Converter & Cleaners")
# st.write("Upload Your CSV and Excel Files to clean the data convert formats effortlessly🧨")

# file = st.file_uploader("Upload CSV or Excel Files", type =["csv","xlsx"],accept_multiple_files=True )
 
# if file:
#   for file in file:
#             ext = file.name.split(".")[-1]
#             df=pd.read_csv(file)if ext== "csv" else pd.read_excel(file)

#             st.subheader(f"🔍{file.name}I -Preview")
#             st.dataframe(df.head())

#             if st.checkbox(f"Fill Missing Values-{file.name}"):
#                   df.fillna(df.select_dtypes(include="number").mean(),inplace= True)
#                   st.success("Missing value filled successfully")
#                   st.dataframe(df.head())

# selected_columns =st.multiselect(f"Select Columns - {file.name}", df.columns, default= df.columns)
# df=df[selected_columns]
# st.dataframe(df.head())

# if st.checkbox(f"Show Chart- {file.name}") and not df.select_dtypes(include ="number").empty: 
#     st.bar_chart(df.select_dtypes(include ="number").iloc[:, :2])

# format_choice =st.radio(f"Convert {file.name} to :",["CSV","Excel"], key =file.name )

# if st.button(f"Download {file.name} as {format_choice}"):
#       output =BytesIO()
#       if format_choice == "CSV":
#          df.to_csv(output, index= False)
#          mime = "text/csv"
#          new_name = file.name.replace(ext,"csv")
#       else:
#           df.to_excel(output= False)
#           mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" 
#           new_name= file.name.replace(ext,"xlsx")
#       output.seek(0)
#       st.download_button("Download File",file_name=  new_name,data= output,mime=mime )
#       st.success("Processing Completed!")
import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📁File-Converter & Cleaners", layout="wide")
st.title("📁File-Converter & Cleaners")
st.write("Upload your CSV and Excel files to clean and convert formats effortlessly 🧨")

uploaded_files = st.file_uploader("Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        ext = uploaded_file.name.split(".")[-1]
        
        # Read file based on extension
        if ext == "csv":
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader(f"🔍 {uploaded_file.name} - Preview")
        st.dataframe(df.head())

        # Fill missing numeric values
        if st.checkbox(f"Fill Missing Values - {uploaded_file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("Missing values filled successfully.")
            st.dataframe(df.head())

        # Column selector
        selected_columns = st.multiselect(
            f"Select Columns - {uploaded_file.name}", df.columns, default=list(df.columns), key=f"cols_{uploaded_file.name}"
        )
        df = df[selected_columns]
        st.dataframe(df.head())

        # Show chart if numeric data exists
        if st.checkbox(f"Show Chart - {uploaded_file.name}") and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # File format conversion
        format_choice = st.radio(
            f"Convert {uploaded_file.name} to:", ["CSV", "Excel"], key=f"format_{uploaded_file.name}"
        )

        if st.button(f"Download {uploaded_file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = uploaded_file.name.rsplit(".", 1)[0] + ".csv"
            else:
                with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                    df.to_excel(writer, index=False, sheet_name="Sheet1")
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = uploaded_file.name.rsplit(".", 1)[0] + ".xlsx"

            output.seek(0)
            st.download_button("📥 Download File", data=output, file_name=new_name, mime=mime)
            st.success("✅ Processing Completed!")
