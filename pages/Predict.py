import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

st.title("🔮 공연 위험도 예측")

# 🔔 여기 추가! — 제목 바로 아래 안내 문구
with st.spinner("모델을 학습하는 중입니다. 잠시만 기다려주세요..."):
    # 모델을 불러오기/학습하기
    @st.cache_resource
    def train_model():
        df = pd.read_excel("SEco.xlsx")

        X = df[['공연장', '장르', '관람인원', 'MONTH']]
        y = df['SEco_norm']

        categorical = ['공연장', '장르']
        numeric = ['관람인원', 'MONTH']

        preprocess = ColumnTransformer([
            ('cat', OneHotEncoder(handle_unknown="ignore"), categorical),
            ('num', 'passthrough', numeric)
        ])

        model = Pipeline([
            ('preprocess', preprocess),
            ('regressor', XGBRegressor(
                n_estimators=300,
                learning_rate=0.1,
                max_depth=5,
                random_state=42
            ))
        ])
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model.fit(X_train, y_train)

        halls = X['공연장'].unique().tolist()
        genres = X['장르'].unique().tolist()
        return model, halls, genres

    model, hall_list, genre_list = train_model()

# ===========================
# 입력 UI
# ===========================

hall = st.selectbox("공연장", hall_list)
genre = st.selectbox("장르", genre_list)
audience = st.slider("관람인원", 100, 100000, 100, step=100)
month = st.selectbox("월", list(range(1, 13)))

if st.button("예측하기"):
    new_data = pd.DataFrame(
        [[hall, genre, audience, month]],
        columns=['공연장', '장르', '관람인원', 'MONTH']
    )

    pred = model.predict(new_data)[0]

    if pred >= 81:
        label = "🚨 5단계 (위험)"
    elif pred >= 61:
        label = "⚡ 4단계 (경계)"
    elif pred >= 41:
        label = "⚠️ 3단계 (주의)"
    elif pred >= 21:
        label = "🌿 2단계 (양호)"
    else:
        label = "🌳 1단계 (안전)"

    st.subheader("📌 예측 결과")
    st.write(f"**SEco 예측치:** {pred:.2f}")
    st.write(f"**위험 등급:** {label}")
