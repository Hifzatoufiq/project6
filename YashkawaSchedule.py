import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Your App Title",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

# ... Your existing code ...

# Custom CSS for styling
custom_css = """
<style>
/* Add your custom CSS styles here */

/* Example styles for the sidebar */
.sidebar .sidebar-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.sidebar img {
    margin-bottom: 10px; /* Add margin to the bottom of the image */
    border-radius: 50%;
}

/* Example styles for the tables */
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #5C5E62;
    color: white;
}
.st-emotion-cache-79elbk eczjsme10{
  background-color: #5C5E62;
}

/* Add more styles as needed */

</style>
"""




st.markdown(custom_css, unsafe_allow_html=True)






# Display the image using the absolute path

st.markdown(custom_css, unsafe_allow_html=True)
#title of the page
st.title("Shedule production work order")
data2 = {
            'order id ': ['1', '2'],
            'Order name<br>(Part description)': ['PICKUP FRAME', 'V6_Gate_Tail'],
            'weekly Quantity': ['50', '50'],
            'Robot ID': ['yakshawa 3', 'yakshawa 4'],
        }
#second dataframe
df2 = pd.DataFrame(data2)
        
styled_df2 = df2.style.hide(axis="index").set_table_styles([
            {'selector': '', 'props': [('background-color', '#262730'), ('color', 'white')]},
            {'selector': 'th', 'props': [('background-color', '#262730'), ('color', 'white')]},
        ])

        # Convert the styled DataFrame to HTML
html_code = styled_df2.to_html(escape=False)

        # Manipulate the HTML string to include the width property
html_code = html_code.replace('<table', '<table style="width:1000px;"')

st.markdown(html_code, unsafe_allow_html=True)
        # Add a horizontal rule with black color
st.markdown("<hr style='border: 2px solid #0E1117;'>", unsafe_allow_html=True)

data2 = {
            'order id ': ['1', '1', '1'],
            'child component<br> name)': ['FANCANTINE-A40-ST1', 'COCLE-A-40-ST1', 'RACCOGLITORE_V6_DX-K56790'],
            'Quantity<br> (needed per Father)': ['1', '1', '1'],
            'Quantity to be produced': ['50', '50', '50'],
        }

df2 = pd.DataFrame(data2)

styled_df2 = df2.style.hide(axis="index").set_table_styles([
            {'selector': '', 'props': [('background-color', '#262730'), ('color', 'white')]},
            {'selector': 'th', 'props': [('background-color', '#262730'), ('color', 'white')]},
        ])

        # Convert the styled DataFrame to HTML
html_code = styled_df2.to_html(escape=False)

        # Manipulate the HTML string to include the width property
html_code = html_code.replace('<table', '<table style="width:1000px;"')

st.markdown(html_code, unsafe_allow_html=True)
