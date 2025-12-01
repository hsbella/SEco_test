import streamlit as st
from PIL import Image

st.title("📊 데이터 시각화")


# -------------------------------
# Helper: 이미지 + 분석문 (왼쪽 정렬)
# -------------------------------
def left_block(img_path, text, ratio=[2, 1]):
    col_left, col_right = st.columns(ratio)
    with col_left:
        st.image(Image.open(img_path), use_column_width=True)
        st.markdown(f"<p style='color:gray;'>{text}</p>", unsafe_allow_html=True)


# -------------------------------
# 1. 월별 전체 위험 시계열
# -------------------------------
st.markdown("##### 📆 월별 전체 위험 시계열(Time Series)")
left_block(
    "monthly_timeseries.jpg",
    "5~7월과 10월에 위험도가 높아지는 계절적 패턴이 나타납니다.",
    ratio=[2, 1]
)
st.markdown("\n\n\n")


# -------------------------------
# 2. 위험등급 분포 Pie chart (가로 비율 1:2)
# -------------------------------
st.markdown("##### 🍩 위험등급 분포 Pie chart")
left_block(
    "risk_heatmap.jpg",
    "전체 공연 중 3·4등급이 69%로 ‘중위험 이상’ 공연이 대부분입니다.",
    ratio=[3, 4]  # ← 파이차트 1:2
)
st.markdown("\n\n\n")


# -------------------------------
# 3. 공연별 위험도 Top 10
# -------------------------------
st.markdown("##### 🎭 공연별 위험도 Top 10")
left_block(
    "bar_risk_top10.jpg",
    "대형 아이돌·밴드 공연 중심으로 높은 위험도가 나타납니다.",
    ratio=[2, 1]
)
st.markdown("\n\n\n")


# -------------------------------
# 4. SVI / HLI / AQHI 월별 비교
# -------------------------------
st.markdown("##### 📈 SVI / HLI / AQHI 월별 비교")
left_block(
    "monthly_3index.jpg",
    "SVI·HLI는 여름·가을에 상승하고 AQHI는 안정적으로 유지됩니다.",
    ratio=[2, 1]
)
st.markdown("\n\n\n")


# -------------------------------
# 5. 월별 위험 Heatmap (가로 비율 1:3, 텍스트 줄바꿈 제거)
# -------------------------------
st.markdown("##### 🔥 월별 위험 Heatmap")

col_left, col_right = st.columns([1, 3])
with col_left:
    st.image(Image.open("monthly_risk.jpg"), use_column_width=True)
    st.markdown(
        "<p style='color:gray; white-space: nowrap;'>5월과 10월이 가장 고위험 구간으로 나타납니다.</p>",
        unsafe_allow_html=True
    )

