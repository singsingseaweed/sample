import streamlit as st
import pandas as pd
import os

# 데이터 파일의 절대 경로
data_file_path = os.path.abspath("data.csv")

# 데이터 가져오기
df = pd.read_csv(data_file_path)

# 웹 애플리케이션 정의
st.title("간단한 데이터 시각화 앱")

# 데이터를 보여주기
st.write(df)

# 막대 차트 표시
st.bar_chart(df['column_name'])
