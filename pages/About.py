import streamlit as st

st.title("모델 설명 (SEco 구성)")

st.markdown("""
### 📌 SEco란?

SafetyEco INDEX로 올림픽공원 공연장(진동·소음)과 스포츠센터(운동강도·공기질·혼잡)를 하나의 ‘안전·환경 통합지수’로 묶어 AI 기반으로 공연 위험도를 자동 예측하는 ESG 기반 시스템입니다.

---

### 🧑‍💻 사용한 데이터

**공공데이터**
- KSPC 올림픽공원 공연장 정보
- KSPC 올림픽공원 운영현황
- KSPC 스포츠센터 월회원 이용현황

**민간데이터**
- 서울특별시 송파구 시간별 미세먼지, 외기질 관리, 계절요인 데이터 (서울열린데이터광장)
- 서울특별시 시간별 기온·습도·강수량 (기상청)
- ACSM MET Compendium – 운동별 MET (운동강도)

---

### 지수 계산 방식
""")

# ---------------------
# SVI
st.markdown("###### 1️⃣ SVI (공연 특성 지수)")

st.latex(r"""
SVI(i) = 100 \times \left[ 
0.5 \cdot w_{\text{genre}}(i) 
+ 0.3 \cdot w_{\text{hall}}(i) 
+ 0.2 \cdot \text{audience\_scaling}(i)
\right]
""")

st.markdown("""
<br>
<small>📎 w_hall = 공연장 가중치, w_genre = 장르 가중치, audience_scaling = 관람인원 스케일링</small>
<br><br><br><br>
""", unsafe_allow_html=True)

# ---------------------
# HLI
st.markdown("###### 2️⃣ HLI (혼잡 부하 지수)")

st.latex(r"""
HLI(i) = 100 \times \left[
0.5 \cdot \text{visitors\_scaling}(i)
+ 0.3 \cdot \text{parking\_scaling}(i)
+ 0.2 \cdot \text{facility\_scaling}(i)
\right]
""")

st.markdown("""
<br>
<small>
📎 visitors_scaling = 방문자수, parking_scaling = 주차량, facility_scaling = 시설 이용량 스케일링</small>
<br><br><br><br>
""", unsafe_allow_html=True)

# ---------------------
# AQHI
st.markdown("###### 3️⃣ AQHI (실내 공기질 지수)")

st.latex(r"""
AQHI =  100 \times \left[
0.5 \cdot CO2_{norm}
+ 0.2 \cdot \left( \frac{\Delta T_{norm} + \Delta H_{norm}}{2} \right)
+ 0.2 \cdot PM_{factor}
+ 0.1 \cdot \text{season\_factor}
\right]
""")

st.markdown("""
<br>
<small>
📎 CO2_norm = CO₂ 증가량 정규화, ΔT_norm = 온도 변화 정규화, ΔH_norm = 습도 변화 정규화, PM_factor = 미세먼지 반영값, season_factor = 계절 보정</small>
<br><br><br><br>
""", unsafe_allow_html=True)

# ---------------------
# SEco
st.markdown("###### 4️⃣ SEco 통합 지수")

st.latex(r"""
CVI = 0.7 \cdot SVI + 0.3 \cdot HLI
""")

st.markdown("""
<br>
<small>
📎 CVI = 공연장·시설 통합 위험도</small>
""", unsafe_allow_html=True)

st.latex(r"""
SEco = 0.5 \cdot CVI + 0.5 \cdot AQHI_{\text{month}}
""")

st.markdown("""
<br>
<small>
📎AQHI_month = 월별 공기질 지수</small>
""", unsafe_allow_html=True)

# ---------------------
st.markdown("""
---

### 💻 사용된 모델: XGBoost Regressor 기반 SEco 예측 모델

본 예측 모델은 공연장 환경·안전 지수(SEco)를 예측하기 위해  
다음과 같은 머신러닝 파이프라인으로 학습되었습니다.

###### 1️⃣ 전처리
- **OneHotEncoder** : 공연장/장르를 벡터로 인코딩  
- **ColumnTransformer** : 범주형 + 수치형 일괄 처리

/n/n/n

###### 2️⃣ 입력 특징 (Features)
| Feature | 설명 |
|--------|------|
| 공연장 | 공연장 종류 |
| 장르 | 공연 장르 |
| 관람 인원 | 관람객 수 |
| MONTH | 공연 월(계절성 반영) |

/n/n/n

###### 3️⃣ 모델 (Regressor)
- **XGBoost Regressor**
- n_estimators = 300  
- learning_rate = 0.1  
- max_depth = 5  

/n/n/n

###### 4️⃣ 출력 (Output)
- **SEco 위험도 (0~100)**  
- 위험도 기반 1~5단계 등급 분류

---

### 📢 위험단계 기준
| SEco 지수 | 단계 |
|--------|------|
| 81~100 | 🚨 5단계 (매우 위험) |
| 61~80 | ⚡ 4단계 (경계) |
| 41~60 | ⚠️ 3단계 (주의) |
| 21~40 | 🌿 2단계 (양호) |
| 0~20 | 🌳 1단계 (안전) |
""")
