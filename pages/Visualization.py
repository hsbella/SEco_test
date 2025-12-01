import streamlit as st
from PIL import Image

st.title("📊 데이터 시각화")

# 공통: 가운데 1열 컬럼 구조
def centered_image(img_path):
    col_left, col_center, col_right = st.columns([1, 3, 1])  # 가운데 넓게
    with col_center:
        st.image(Image.open(img_path), use_column_width=True)


# -------------------------------
# 1. 월별 전체 위험 시계열
# -------------------------------
st.markdown("##### 📆 월별 전체 위험 시계열(Time Series)")
centered_image("monthly_timeseries.jpg")

st.markdown(
    "<p style='text-align:center; color:gray;'>5~7월과 10월에 위험도가 높아지는 계절적 패턴이 나타납니다.</p>",
    unsafe_allow_html=True
)

st.markdown("\n\n\n")


# -------------------------------
# 2. 위험등급 분포 Pie chart
# -------------------------------
st.markdown("##### 🍩 위험등급 분포 Pie chart")
centered_image("risk_heatmap.jpg")

st.markdown(
    "<p style='text-align:center; color:gray;'>전체 공연 중 3·4등급이 69%로, ‘중위험 이상’ 공연이 대부분입니다.</p>",
    unsafe_allow_html=True
)

st.markdown("\n\n\n")


# -------------------------------
# 3. 공연별 위험도 Top 10
# -------------------------------
st.markdown("##### 🎭 공연별 위험도 Top 10")
centered_image("bar_risk_top10.jpg")

st.markdown(
    "<p style='text-align:center; color:gray;'>대형 아이돌·밴드 공연 중심으로 높은 위험도가 나타나며, 관람객 규모와 장르 영향이 큽니다.</p>",
    unsafe_allow_html=True
)

st.markdown("\n\n\n")


# -------------------------------
# 4. SVI / HLI / AQHI 월별 비교
# -------------------------------
st.markdown("##### 📈 SVI / HLI / AQHI 월별 비교")
centered_image("monthly_3index.jpg")

st.markdown(
    "<p style='text-align:center; color:gray;'>SVI·HLI는 여름·가을에 상승하고 AQHI는 안정적이며, 계절·장르·혼잡도의 복합 영향이 확인됩니다.</p>",
    unsafe_allow_html=True
)

st.markdown("\n\n\n")


# -------------------------------
# 5. 월별 위험 Heatmap
# -------------------------------
st.markdown("##### 🔥 월별 위험 Heatmap")
centered_image("monthly_risk.jpg")

st.markdown(
    "<p style='text-align:center; color:gray;'>5월과 10월이 가장 고위험 구간으로, 공기질·혼잡·진동이 동시에 높게 나타나는 달입니다.</p>",
    unsafe_allow_html=True
)
