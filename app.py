
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="WORK TALK", layout="wide")
st.image("WORK_TALK_small.png", use_container_width=True)

st.markdown("### 📋 작업 사진 + 위험성평가 설문 입력")
st.markdown("사진 1장 업로드 → 질문 4개 응답 → 저장 → 다음 사진 순서대로 진행해 주세요.")

# 임시 저장소 (로컬용)
if "responses" not in st.session_state:
    st.session_state.responses = []

name = st.text_input("👤 이름")
dept = st.text_input("🏢 부서")
photo = st.file_uploader("📸 작업 사진 업로드", type=["jpg", "jpeg", "png"])

if photo:
    st.image(photo, width=300)
    q1 = st.text_input("1️⃣ 어떤 작업을 하고 있는 건가요?")
    q2 = st.text_input("2️⃣ 이 작업은 왜 위험하다고 생각하나요?")
    q3 = st.radio("3️⃣ 이 작업은 얼마나 자주 하나요?", ["연 1-2회", "반기 1-2회", "월 2-3회", "주 1회 이상", "매일"])
    q4 = st.radio("4️⃣ 이 작업은 얼마나 위험하다고 생각하나요?", [
        "약간의 위험: 일회용 밴드 치료 필요 가능성 있음",
        "조금 위험: 병원 치료 필요. 1-2일 치료 및 휴식",
        "위험: 보름 이상의 휴식이 필요한 중상 가능성 있음",
        "매우 위험: 불가역적 장애 또는 사망 가능성 있음"
    ])

    if name and dept and q1 and q2 and q3 and q4:
        if st.button("📥 저장하기"):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.responses.append({
                "작성일시": now,
                "이름": name,
                "부서": dept,
                "사진": photo.name,
                "질문1": q1,
                "질문2": q2,
                "질문3": q3,
                "질문4": q4
            })
            st.success("✅ 저장 완료! 다음 사진을 업로드해 주세요.")

if st.session_state.responses:
    df = pd.DataFrame(st.session_state.responses)
    st.markdown("---")
    st.markdown("### 📊 입력된 응답 미리보기 (테스트용)")
    st.dataframe(df)
