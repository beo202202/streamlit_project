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

wav_file = st.file_uploader("UPLOAD WAV FILE")

st.info(
    f"""
            👆 Upload a .wav file. Or try a sample: [Wav sample 01](https://github.com/CharlyWargnier/CSVHub/blob/main/Wave_files_demos/Welcome.wav?raw=true)
            """
)

option = st.selectbox('Please select in selectbox!', 
                      ('강민철 튜터님', '추후 추가1', '추후 추가2'))
	
st.write('You selected:', option)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Info")


with st.spinner('Wait for it...'):
    time.sleep(1)
st.success('Done!')

if st.button("click button"):
    st.write("Data Loading..")
    # 데이터 로딩 함수는 여기에!

audio_file = open('Buzz(버즈) - 겁쟁이.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)