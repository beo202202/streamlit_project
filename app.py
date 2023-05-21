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

# 페이지 헤더, 서브헤더 제목 설정
st.header("준영이의 페이지에 오신걸 환영합니다.✌")
st.subheader("스트림릿 기능 맛보기")

# 페이지 칼럼 분할(예: 부트스트랩 컬럼, 그리드)
cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 ℃", "2")
cols[0].metric("10/12", "17 ℃", "2 ℉")
cols[0].metric("10/13", "15 ℃", "2")
cols[1].metric("10/14", "17 ℃", "2 ℉")
cols[1].metric("10/15", "14 ℃", "-3 ℉")
cols[1].metric("10/16", "13 ℃", "-1 ℉")

# 라인 그래프 데이터 생성(with. Pandas)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# 칼럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)
