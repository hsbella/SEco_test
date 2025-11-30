import streamlit as st
from PIL import Image

st.title("📊 데이터 시각화")


st.markdown("##### 📈 월별 전체 위험 시계열(Time Series)")
st.image(Image.open("monthly_timeseries.jpg"), use_column_width=True)

st.markdown("\n\n\n")  

st.markdown("##### 🔥월별 위험 Heatmap")
st.image(Image.open("risk_heatmap.jpg"), use_column_width=True)

st.markdown("\n\n\n")  

st.markdown("##### 🎭 공연별 위험도 Top 10")
st.image(Image.open("bar_risk_top10.jpg"), use_column_width=True)

st.markdown("\n\n\n")  

st.markdown("##### 📈 SVI / HLI / AQHI 월별 비교")
st.image(Image.open("monthly_3index.jpg"), use_column_width=True)

st.markdown("\n\n\n")  

st.markdown("##### 📉 월별 SEco 위험 점수")
st.image(Image.open("monthly_risk.jpg"), use_column_width=True)
