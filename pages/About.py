import streamlit as st

st.title("모델 설명 (SEco 구성)")

st.markdown("""
### 📌 SEco란?

SafetyEco INDEX로 올림픽공원 공연장(진동·소음)과 스포츠센터(운동강도·공기질·혼잡)를 하나의 ‘안전·환경 통합지수로 묶어 AI 기반으로 공연 위험도를 자동 예측하는 ESG 기반 시스템입니다.

---

### 🧑‍💻 사용한 데이터
**공공데이터**
- KSPC 올림픽공원 공연장 정보
- KSPC 올림픽공원 운영현황
- KSPC 스포츠센터 월회원 이용현황

**민간데이터**
- 서울특별시 송파구 시간별 미세먼지, 외기질 관리, 계절요인 데이터(서울열린데이터광장)
- 서울특별시 시간별 기온, 습도, 강수량 데이터 (기상청)
- ACSM MET Compendium- 운동별 운동강도(MET) (ACSM미국스포츠의학회)

---

### 지수 계산 방식

- SVI
**SVI(i) = 100 * [ 0.5 * w_genre(i) + 0.3 * w_hall(i) + 0.2 * audience_scaling(i) ]**
* w_hall = 공연장 가중치, w_genre = 장르 가중치, audience_scaling = 관람인원 스케일링

- HLI
**HLI(i) = 100 * [ 0.5 * visitors_scaling(i) + 0.3 * parking_scaling(i) + 0.2 * facility_scaling(i) ] **
* visitors_scaling = 방문자수 스케일링, parking_scaling = 주차량 스케일링, facility_scaling = 시설이용량 스케일링

- AQHI
!!!!!!!!!!정리필요!!!!!!!!!!!!!!!!

- SEco
**CVI = 0.7*SVI_lite + 0.3*HLI_lite**
* CVI = 공연장 통합 위험도 (CVI)

**SEco = 0.5*CVI + 0.5*AQHI_month**

---
## 💻 사용된 모델 : XGBoost Regressor
- OneHotEncoder + ColumnTransformer 전처리
- 관람 인원 / 장르 / 공연장 / MONTH 을 입력
- 위험도(0~100)을 출력

---

## 📢 위험등급 산정 기준
| 위험도 | 등급 |
|--------|------|
| 81~100 | 🚨 매우 위험 |
| 61~80 | ⚡ 경계 |
| 41~60 | ⚠️ 주의 |
| 21~40 | 🌿 양호 |
| 0~20 | 🌳 안전 |

""")
