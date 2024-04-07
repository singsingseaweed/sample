import streamlit as st

# 타이틀 추가
st.title('나의 첫 Streamlit 앱')

# 텍스트 추가
st.write('안녕하세요! 이것은 Streamlit으로 만든 첫 웹 페이지입니다.')

# 그래프 추가
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)
plt.hist(data, bins=20)
st.pyplot()

# 사이드바에 입력 필드 추가
name = st.sidebar.text_input('이름 입력', '이름을 입력하세요')
st.sidebar.write('안녕하세요,', name, '님!')

# 다양한 위젯 추가
number = st.number_input('숫자 입력', value=10)
st.write('입력된 숫자는', number, '입니다.')

# 버튼 추가
if st.button('버튼을 클릭하세요'):
    st.write('버튼이 클릭되었습니다!')

# 파일 업로드 기능 추가
uploaded_file = st.file_uploader('파일 업로드', type=['txt', 'csv'])
if uploaded_file is not None:
    st.write('파일이 성공적으로 업로드 되었습니다.')

# 외부 링크 추가
st.write('OpenAI의 웹사이트를 방문해보세요:', '[OpenAI 웹사이트](https://openai.com)')

# 맵 추가
st.map()
