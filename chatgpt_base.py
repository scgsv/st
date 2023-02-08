%%writefile streamlit_app.py 
import streamlit as st
import pandas as pd
import plotly.express as px
st.write('# Avocado Prices dashboard')  #st.title('Avocado Prices dashboard')
# https://markdown-editor.github.io/   This will help build markdown
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')
st.header('Summary statistics')
st.header('Line chart by geographies')
st.header('Summary statistics')
avocado = pd.read_csv('https://raw.githubusercontent.com/fenago/datasets/main/avocado-updated-2020.csv')
avocado_stats = avocado.groupby('type')['average_price'].mean()
st.dataframe(avocado_stats)
st.header('Line chart by geographies')
line_fig = px.line(avocado[avocado['geography'] == 'Los Angeles'],
                   x='date', y='average_price',
                   color='type',
                   title='Avocado Prices in Los Angeles')
st.plotly_chart(line_fig)
selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
submitted = st.button('Submit')
if submitted:
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    st.plotly_chart(line_fig)

with st.form('line_chart'):
    selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
    submitted = st.form_submit_button('Submit')
    if submitted:
        filtered_avocado = avocado[avocado['geography'] == selected_geography]
        line_fig = px.line(filtered_avocado,
                           x='date', y='average_price',
                           color='type',
                           title=f'Avocado Prices in {selected_geography}')
        st.plotly_chart(line_fig)

with st.sidebar:
    st.subheader('About')
    st.markdown('Data Analytics / Data Science Assistant:  Miami Dade College')
        
st.sidebar.image('https://clipground.com/images/miami-dade-college-logo-7.png', width=50)

@st.cache
def load_data(path):
    dataset = pd.read_csv(path)
    return dataset
avocado = load_data('https://raw.githubusercontent.com/fenago/datasets/main/avocado-updated-2020.csv')

# display dataframe as a table
df = pd.read_csv('https://raw.githubusercontent.com/fenago/datasets/main/avocado-updated-2020.csv')
st.dataframe(df)
