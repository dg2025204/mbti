import streamlit as st
import time
import random

# 1. 페이지 기본 설정 (가장 먼저 와야 합니다 - 'wide' 레이아웃으로 변경)
st.set_page_config(page_title="초호화 MBTI 포켓몬", page_icon="✨", layout="wide")

# 2. 극도로 화려한 커스텀 CSS 적용 (애니메이션, 그라데이션, 그림자 효과)
st.markdown("""
<style>
    /* 움직이는 그라데이션 배경 */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fecfef, #a1c4fd, #c2e9fb);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    /* 네온사인처럼 빛나는 제목 */
    .glowing-title {
        font-size: 55px;
        color: #ffffff;
        text-align: center;
        font-weight: 900;
        text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #ff00de, 0 0 40px #ff00de;
        animation: blink 2s infinite alternate;
        margin-bottom: 10px;
    }
    @keyframes blink {
        100% {text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6, 0 0 50px #ff4da6;}
    }

    /* 서브 타이틀 */
    .sub-title {
        font-size: 22px;
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        background-color: rgba(255, 255, 255, 0.6);
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 30px;
    }

    /* 포켓몬 결과 카드 디자인 */
    .poke-card {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 30px;
        padding: 30px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        text-align: center;
        border: 5px solid #ffde00;
        transition: transform 0.3s;
    }
    .poke-card:hover {
        transform: scale(1.03);
    }

    /* 화려한 그라데이션 버튼 */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff8a00, #e52e71);
        color: white;
        font-size: 26px;
        font-weight: 900;
        border-radius: 50px;
        border: none;
        width: 100%;
        height: 70px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-5px);
        box-shadow: 0px 15px 25px rgba(0,0,0,0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. 화면 구성
st.markdown('<div class="glowing-title">🌟 초호화 MBTI 포켓몬 도감 🌟</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당곡고등학교 친구들! 우주에서 제일 화려한 포켓몬 도감에 온 걸 환영해! 🎉</div>', unsafe_allow_html=True)

# 4. 포켓몬 데이터 (도감 번호, 설명에 추가로 가상의 '능력치' 데이터 추가)
pokemon_data = {
    "ISTJ": {"name": "이상해씨", "desc": "성실하고 책임감 넘치는 이상해씨! 듬직한 당신과 꼭 닮았어요 🌿", "img": "1", "hp": 80, "atk": 60, "charm": 70},
    "ISFJ": {"name": "럭키", "desc": "따뜻하고 배려심 깊은 럭키! 주변 사람을 잘 챙기는 천사 같아요 🥚", "img": "113", "hp": 95, "atk": 30, "charm": 100},
    "INFJ": {"name": "라프라스", "desc": "신비롭고 통찰력 있는 라프라스! 부드러우면서도 강인한 내면을 가졌어요 🌊", "img": "131", "hp": 85, "atk": 70, "charm": 90},
    "INTJ": {"name": "뮤츠", "desc": "전략적이고 독립적인 뮤츠! 똑똑하고 계획적인 완벽주의자네요 🔮", "img": "150", "hp": 90, "atk": 100, "charm": 60},
    "ISTP": {"name": "잠만보", "desc": "만사 귀찮지만 내공이 엄청난 잠만보! 효율성을 중시하는 당신에게 딱이에요 💤", "img": "143", "hp": 100, "atk": 90, "charm": 50},
    "ISFP": {"name": "이브이", "desc": "자유롭고 예술적인 이브이! 어떤 모습으로든 진화할 수 있는 무궁무진한 매력 🌟", "img": "133", "hp": 60, "atk": 60, "charm": 95},
    "INFP": {"name": "뮤", "desc": "상상력이 풍부하고 이상주의적인 뮤! 호기심 많고 순수한 영혼이에요 🌸", "img": "151", "hp": 80, "atk": 80, "charm": 100},
    "INTP": {"name": "폴리곤", "desc": "논리적이고 지적 호기심이 많은 폴리곤! 분석하고 탐구하는 것을 좋아해요 💻", "img": "137", "hp": 70, "atk": 75, "charm": 55},
    "ESTP": {"name": "리자몽", "desc": "행동력 갑! 에너제틱한 리자몽! 스릴을 즐기고 어디서나 당당해요 🔥", "img": "6", "hp": 75, "atk": 95, "charm": 80},
    "ESFP": {"name": "푸린", "desc": "관심받기 좋아하고 흥이 많은 푸린! 분위기 메이커인 당신은 인싸 중의 인싸 🎤", "img": "39", "hp": 90, "atk": 40, "charm": 100},
    "ENFP": {"name": "피카츄", "desc": "에너지 넘치고 발랄한 피카츄! 특유의 친화력으로 주변을 항상 밝게 만들어요 ⚡", "img": "25", "hp": 60, "atk": 75, "charm": 95},
    "ENTP": {"name": "팬텀", "desc": "장난기 많고 재치 넘치는 팬텀! 통통 튀는 아이디어로 사람들을 놀라게 해요 👻", "img": "94", "hp": 65, "atk": 85, "charm": 80},
    "ESTJ": {"name": "거북왕", "desc": "규칙을 잘 지키고 리더십 있는 거북왕! 든든하고 체계적인 당신을 닮았어요 🐢", "img": "9", "hp": 85, "atk": 80, "charm": 65},
    "ESFJ": {"name": "토게피", "desc": "사교적이고 공감 능력이 뛰어난 토게피! 친구들에게 행복을 전해주는 요정 🐣", "img": "175", "hp": 70, "atk": 30, "charm": 100},
    "ENFJ": {"name": "망나뇽", "desc": "부드러운 카리스마로 사람들을 이끄는 망나뇽! 정이 많고 다정한 리더네요 🐉", "img": "149", "hp": 90, "atk": 95, "charm": 85},
    "ENTJ": {"name": "갸라도스", "desc": "목표를 향해 거침없이 돌진하는 갸라도스! 카리스마 넘치는 지휘관 스타일 🌊", "img": "130", "hp": 85, "atk": 100, "charm": 70}
}

# 5. 화면 레이아웃 분할 (양옆 여백을 주어 가운데 정렬 효과)
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    mbti_types = list(pokemon_data.keys())
    selected_mbti = st.selectbox("🔮 당신의 MBTI를 골라주세요!", mbti_types)
    st.write("") # 빈 칸 추가

    if st.button("✨ 내 포켓몬 소환하기! ✨"):
        # 로딩 프로그레스 바 
        progress_text = "마스터볼을 던지는 중... 🔴"
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.015)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.5)
        my_bar.empty() # 로딩바 숨기기
        
        # 팝업 알림(토스트) 효과
        st.toast('야생의 포켓몬이 나타났다!', icon='🎉')
        
        # 이펙트 팡팡! (풍선과 눈송이를 동시에)
        st.balloons()
        if "I" in selected_mbti or "T" in selected_mbti:
            st.snow() 
            
        result = pokemon_data[selected_mbti]
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{result['img']}.png"
        
        # 화려한 카드 UI 안에 결과 출력
        st.markdown('<div class="poke-card">', unsafe_allow_html=True)
        
        st.markdown(f"<h2 style='color: #ff00de; font-weight: 900;'>🎊 {selected_mbti} 찰떡 포켓몬: {result['name']} 🎊</h2>", unsafe_allow_html=True)
        
        # 이미지와 스탯을 2단으로 나누어 보여줌
        img_col, stat_col = st.columns([1, 1])
        
        with img_col:
            st.image(img_url, use_column_width=True)
            
        with stat_col:
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.subheader("📊 포켓몬 능력치")
            st.write("❤️ 체력 (체력장 등급)")
            st.progress(result["hp"])
            st.write("⚔️ 공격력 (학업 열정)")
            st.progress(result["atk"])
            st.write("✨ 매력 (친구들에게 인기)")
            st.progress(result["charm"])
            
        st.markdown(f"<h3 style='color: #2c3e50; background-color: #f1c40f; padding: 10px; border-radius: 10px;'>{result['desc']}</h3>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.success("포켓몬 포획 성공! 이 화면을 캡처해서 친구들에게 자랑해보세요 📸")
