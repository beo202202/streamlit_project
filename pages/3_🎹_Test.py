import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설정
st.set_page_config(
    page_icon="👀",  # win + .
    page_title="준영이의 스트림릿 배포해보기",
    layout="wide",
)

wav_file = st.file_uploader("UPLOAD WAV FILE")

st.info(
    f"""
            👆 Upload a .wav file. Or try a sample: [Wav sample 01](https://github.com/CharlyWargnier/CSVHub/blob/main/Wave_files_demos/Welcome.wav?raw=true)
            """
)