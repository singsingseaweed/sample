import streamlit as st
import pandas as pd

# 데이터 가져오기
df = pd.read_csv("data.csv")

# 웹 애플리케이션 정의
st.title("간단한 데이터 시각화 앱")

# 데이터를 보여주기
st.write(df)

# 막대 차트 표시
st.bar_chart(df['column_name'])
