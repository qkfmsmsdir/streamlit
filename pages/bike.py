import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속중')
data = pd.read_csv("공공자전거.csv")

st.title('공공자전거 어디있지?')

data = data.copy().fillna(0)
data.loc[:,'size'] = 5*(data['LCD']+data['QR'])


color = {'QR':'#52cef7',
         'LCD':'#fa98bb'}
data.loc[:,'color'] = data.copy().loc[:,'운영방식'].map(color)

selected_gu = st.multiselect("자치구를 선택하세요", options=data['자치구'].unique(), default=[], key="gu_select")

if selected_gu:
    filtered_data = data[data['자치구'].isin(selected_gu)]
else:
    filtered_data = data 
    
st.map(filtered_data, latitude="위도", longitude="경도", size="size", color="color")
st.subheader("공공자전거 보관소 주소")
st.dataframe(filtered_data)
