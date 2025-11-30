import streamlit as st

st.set_page_config(page_title="SEco Dashboard", layout="wide")

st.markdown("""
# **SEco**  
### **: 올림픽공원 공연 위험도 예측 시스템**
""")

st.markdown("""

---

\n\n\n\n\n ### 👋 올공지기 웹사이트에 오신 것을 환영합니다 👋


공연장(진동·혼잡·공기질) 데이터 통합 기반 위험도 예측 플랫폼입니다.

---
""")

st.markdown("""
### 💁 사용 가이드
- **About**<br>SEco 알고리즘 및 데이터 처리 구조  
- **Predict**<br>Streamlit 기반 UI로 빠른 위험도 예측  
- **Visualization**<br>월별 시계열·Heatmap·공연별 위험도·지수 비교·Pie chart 시각화 제공
""", unsafe_allow_html=True)





