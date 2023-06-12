import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="202021025 임수창",
)

st.header("제어공학 기말 202021025 임수창")
st.subheader("2번문제:")
st.subheader('''다음 전달함수 G(s) = 100 / (s+2)(s+3)일때  폐루프 전달함수를 구하고 unit step 입력의 응답곡선을 그리고, 주파수 응답을 보드선도로 그리시오. 이것을 자신의 학번 이름을 streamlit을 통해 Web에 배포 하시오. 
''')
st.subheader("")
st.subheader("")
st.subheader('''===================================================''')
st.subheader("")
st.subheader("")
st.subheader('''폐루프 전달함수M(s)를 구하는 과정:''')
st.subheader('''폐루프 전달함수 M(s)=G(s)/1+G(s)H(s)이고, H(s)는 1이라고 본다. 그러면 M(s)=100/s**2+5s+106이 된다''')
