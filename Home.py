import streamlit as st

st.set_page_config(page_title="SEco Dashboard", layout="wide")

st.markdown("""
# **SEco**  
### **: 올림픽공원 공연 위험도 예측 시스템**
""")

st.markdown("""

---

\n\n\n ### 👋 올공지기 웹사이트에 오신 것을 환영합니다 👋


공연장(진동·혼잡·공기질) 데이터 통합 기반 위험도 예측 플랫폼입니다.

\n\n\n\n\n\n\n\n\n\n\n\n\n **SEco 시스템**은 직관에 의존하던 공연장·체육시설의 안전관리를 **데이터 기반 정량지수로 표준화**해, 운영자가 **근거 기반**으로 **위험 대응과 정책 결정**을 할 수 있도록 돕는 예측 시스템입니다.

---
""")

st.markdown("""
### 💁 사용 가이드
- **About**<br> 모델 설명 : SEco 알고리즘 및 데이터 처리 구조  
- **Predict**<br> 예측 모델 : ML 기반 SEco 위험도 예측 모델  
- **Visualization**<br> 데이터 시각화 : 월별 시계열·Pie chart·공연별 위험도·지수 비교·Heatmap 시각화 제공
""", unsafe_allow_html=True)
















