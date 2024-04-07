import streamlit as st

# Streamlit 애플리케이션 제목 설정
st.title("간단한 이름 입력 앱")

# 사용자로부터 이름 입력 받기
name = st.text_input("이름을 입력하세요")

# 입력된 이름이 비어 있지 않은 경우에만 실행
if name:
    # 입력된 이름을 화면에 출력
    st.write(f"안녕하세요, {name}님!")

# 입력 필드 아래에 간단한 안내 메시지 표시
st.write("이름을 입력하고 엔터를 누르면 화면에 표시됩니다.")
