import streamlit as st
import pandas as pd
import numpy as np

# from time import sleep
import time

# 페이지 기본 설정
st.set_page_config(
    page_icon="👀",  # win + .
    page_title="준영이의 스트림릿 배포해보기",
    layout="wide",
)
add_selectbox = st.sidebar.selectbox("분리 옵션 선택", ("2", "4", "5"))
if add_selectbox == "2":
    descrip = "보컬과 그외"
elif add_selectbox == "4":
    descrip = "보컬, 드럼, 베이스, 그외"
elif add_selectbox == "5":
    descrip = "보컬, 드럼, 베이스, 피아노, 그외"
st.sidebar.write("출력: ", descrip)

mp3_file = st.file_uploader("UPLOAD MP3 FILE", type="mp3")
with st.spinner('mp3 파일 기다리는 중...'):
    if mp3_file:
        st.success("Success")
    else:
        time.sleep(1)


st.info(
    f"""
    👆 Upload a .mp3 file.
    """
)

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)
        
        # st.success('Done!')

if st.button("다운로드"):
    st.write("Data Loading..")
    # 데이터 로딩 함수는 여기에!

# audio_file = open('Buzz.mp3', 'rb')
# audio_bytes = audio_file.read()

# st.audio(audio_bytes, format='audio/mp3')


# with open("flower.png", "rb") as file:
#     btn = st.download_button(
#             label="Download image",
#             data=file,
#             file_name="flower.png",
#             mime="image/png"
#           )