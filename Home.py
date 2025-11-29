import streamlit as st

st.set_page_config(page_title="SEco Dashboard", layout="wide")

st.title(" SEco : 올림픽공원 공연 위험도 예측 시스템 ")
st.markdown("""
### 👋 올공지기 웹사이트에 오신 것을 환영합니다 👋


공연장(진동·혼잡·공기질) 데이터 통합 기반 위험도 예측 플랫폼입니다.

---

### 💁 사용 가이드
- **About : 모델 설명** — SEco 알고리즘 및 데이터 처리 구조 
- **Predict : 예측 모델** — Streamlit 기반 UI로 빠른 위험도 예측  
- **Visualization : 데이터 시각화** — 월별 전체 위험 시계열/Heatmap, 공연별 위험도 막대그래프, SVI / HLI / AQHI의 월별 비교 그래프, 위험등급 분포 Pie chart 
""")
