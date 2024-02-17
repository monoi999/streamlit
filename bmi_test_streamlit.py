# 1.필요한 라이브러리 호출
import streamlit as st             # 설치필요=> pip install streamlit
import pandas as pd                # penguins.csv 파일 호출 목적
import datetime                    # 페이지 작성 날짜 출력 목적

# 2.웹 APP의 타이틀 설정           # 웹브라우져의 탭 타이틀 및 emoji 설정
st.set_page_config(                # 웹 페이지의 기본(config) 설정(set)
    page_icon = ":apple:",      # 웹의 탭에 보이는 emoji 선택 => :seedling: (새싹이미지)
    page_title = "BMI계산기"  # 웹 탭에 보이는 웹의 타이틀
)

# 3.페이지 타이틀 및 Header출력
now = datetime.datetime.now()      # 현재 시각/날짜 알려주는 객체(now) 생성
now = now.strftime("%Y/%m/%d")     # 객체(now)의 format을 년/월/일로 변경
st.title("비만도(BMI) Web App")# 웹 페이지상의 첫 제목(가장 큰 font) 출력
st.header("Streamlit으로 Web App만들기 2편")# 제목 아래 머릿글 출력
st.subheader("Date:{}".format(now))# 머릿글 아래 날짜 출력

# 4.BMI 계산 함수
def bmi_calculator(weight, height):# 체중과 신장을 매개변수(전달값)으로 받음
    bmi = weight / (height**2)     # 체중을 신장의 제곱으로 나눈 값을 bmi에 입력
    return bmi                     # bmi를 반환

# 5.체중과 신장을 입력하는 위젯 생성
st.markdown("---")                 # 화면에 경계선 생성

## 5-1.체중을 입력하는 number_input 위젯 생성
weight = st.number_input(label = "체중(단위 kgf)입력:",       # 위젯 라벨 
                        min_value = 0.00, max_value = 300.00, # 입력 최소/최대값 설정
                        value = 0.00,                         # 입력 창에 입력된 default값
                        placeholder = "kgf단위로 입력하세요!")# 입력 창에 아무것도 없을 때, 뜨는 메세지
## 5-1.체중을 입력하는 number_input 위젯 생성
height = st.number_input(label = "신장(단위 m)입력:",         # 위젯 라벨 
                        min_value = 0.00, max_value = 4.00,   # 입력 최소/최대값 설정
                        value = 0.00,                         # 입력 창에 입력된 default값
                        placeholder = "m단위로 입력하세요!")  # 입력 창에 아무것도 없을 때, 뜨는 메세지
## 5-3.BMI계산기를 실행하는 버튼 생성
button = st.button(label = "BMI계산")                         # 위젯 라벨               

if weight >= 200.00 or height >= 2.50:                        # 체중/신장이 너무 크면 
    st.warning("입력된 체중 혹은 신장이 너무 큰 값입니다!!")  # 경고 메세지 생성
elif weight <= 5.00 or height <= 0.50:                        # 체중/신장이 너무 작으면 
    st.warning("입력된 체중 혹은 신장이 너무 작은 값입니다!!")# 경고 메세지 생성

if button:                                                    # BMI계산기 실행 버튼을 누르면
    bmi = round(bmi_calculator(weight, height), 1)            # bmi_calculator함수 실행, 결과값을 bmi로 반환
    st.markdown("**BMI:{}**".format(bmi))                     # bmi값을 출력 : ** **은 bold 효과 발생
    if bmi >= 25.0:                                           # bmi가 25.0이상이면 
        st.markdown(":fire: **:red[과체중]**")                # "fire"이미지, 붉은색의 "과체중" 출력
    elif bmi >= 18.5:                                         # bmi가 25.0미만 18.5이상이면
        st.markdown(":thumbsup: **:green[정상]**")            # "thumbsup"이미지, 녹색의 "정상" 출력
    else:                                                     # 나머지 bmi값에 대해서..
        st.markdown(":warning: **:orange[저체중]**")          # "warning"이미지, 오렌지색의 "저체중" 출력

## [출처] [파이썬 응용:순한 맛] Streamlit(2):비만도(BMI) 측정 Web App 만들기|작성자 코딩 연금술사
