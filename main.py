import streamlit as st
import time
import random

# 1. 페이지 설정
st.set_page_config(page_title="홀로그램 MBTI 포켓몬", page_icon="🌌", layout="wide")

# 2. 새로운 디자인 (네온 우주 다크 테마 & 5가지 댄스 애니메이션)
st.markdown("""
<style>
    /* 🌌 우주 느낌의 움직이는 어두운 배경 */
    .stApp {
        background: linear-gradient(270deg, #11052C, #3D087B, #270082, #000000);
        background-size: 800% 800%;
        animation: cosmicBg 15s ease infinite;
        color: white;
    }
    @keyframes cosmicBg {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* ✨ 빛나는 네온 텍스트 */
    .neon-text {
        color: #fff;
        text-shadow: 0 0 10px #fff, 0 0 20px #0fa, 0 0 40px #0fa, 0 0 80px #0fa;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .sub-text {
        color: #0fa;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 40px;
        font-weight: bold;
        text-shadow: 0 0 5px #0fa;
    }

    /* 🃏 포켓몬 레어 카드 (홀로그램 효과) */
    .holo-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 255, 255, 0.5);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.4), inset 0 0 20px rgba(255, 0, 255, 0.3);
        text-align: center;
        margin-top: 20px;
    }

    /* 포켓몬 이미지 기본 스타일 */
    .poke-img {
        display: block;
        margin: 0 auto;
        width: 100%;
        max-width: 350px;
        filter: drop-shadow(0px 0px 20px rgba(255, 255, 255, 0.6));
    }

    /* =========================================
       🕺 무작위로 선택될 5가지 댄스 애니메이션 🕺
       ========================================= */
       
    /* 1. 바운스 (위아래로 폴짝폴짝) */
    @keyframes bounce {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-25px) scale(1.05); }
    }
    .dance-bounce { animation: bounce 0.5s ease-in-out infinite; }

    /* 2. 쉐이크 스핀 (돌면서 흔들기) */
    @keyframes shake-spin {
        0% { transform: rotate(0deg); }
        25% { transform: rotate(15deg); }
        50% { transform: rotate(0deg); }
        75% { transform: rotate(-15deg); }
        100% { transform: rotate(360deg); }
    }
    .dance-shake-spin { animation: shake-spin 1s linear infinite; }

    /* 3. 펄스 (심장 박동처럼 커졌다 작아지기) */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2) rotate(5deg); }
    }
    .dance-pulse { animation: pulse 0.6s ease-in-out infinite; }

    /* 4. 스윙 (시계추처럼 좌우로 흔들기) */
    @keyframes swing {
        0%, 100% { transform: rotate(0deg); transform-origin: top center; }
        33% { transform: rotate(15deg); transform-origin: top center; }
        66% { transform: rotate(-15deg); transform-origin: top center; }
    }
    .dance-swing { animation: swing 0.8s ease-in-out infinite; }

    /* 5. 젤리 (꿀렁거리기) */
    @keyframes jelly {
        0%, 100% { transform: scale(1, 1); }
        25% { transform: scale(1.15, 0.85); }
        50% { transform: scale(0.85, 1.15); }
        75% { transform: scale(1.05, 0.95); }
    }
    .dance-jelly { animation: jelly 0.7s infinite; }

    /* 사이버펑크 스타일 버튼 */
    div.stButton > button:first-child {
        background: transparent;
        color: #0fa;
        border: 2px solid #0fa;
        border-radius: 10px;
        font-size: 1.5rem;
        font-weight: bold;
        padding: 15px 0;
        width: 100%;
        box-shadow: 0 0 10px #0fa, inset 0 0 10px #0fa;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background: #0fa;
        color: #000;
        box-shadow: 0 0 20px #0fa, inset 0 0 20px #0fa;
        transform: scale(1.02);
    }
    
    /* 어두운 테마에 맞춘 스토리 텍스트 창 */
    .story-text-dark {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #eeeeee;
        text-align: left;
        background: rgba(0, 0, 0, 0.6);
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
        border-left: 5px solid #0fa;
        box-shadow: 0 4px 15px rgba(0, 255, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 3. 타이틀 영역
st.markdown('<div class="neon-text">🌌 은하계 MBTI 포켓몬 🌌</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">당곡고등학교 학생들을 위한 홀로그램 심리 도감 🚀</div>', unsafe_allow_html=True)

# 4. 방대한 포켓몬 데이터 딕셔너리
pokemon_data = {
    "ISTJ": {"name": "이상해씨", "title": "원칙주의자 모범생", "img": "1", "stats": [85, 70, 60], "desc": "한 번 정한 목표는 흔들림 없이 밀고 나가는 듬직한 이상해씨입니다. 당곡고에서 당신은 항상 필기가 완벽하고, 수행평가 기한을 절대 어기지 않는 철저한 모범생 스타일이에요!"},
    "ISFJ": {"name": "럭키", "title": "다정한 수호천사", "img": "113", "stats": [100, 30, 95], "desc": "친구들이 힘들 때 가장 먼저 다가가 조용히 위로를 건네는 럭키입니다. 반에서 당신이 없으면 교실 분위기가 삭막해질 정도로 당신의 존재감은 큽니다."},
    "INFJ": {"name": "라프라스", "title": "심연의 통찰가", "img": "131", "stats": [80, 60, 90], "desc": "조용하지만 날카로운 통찰력을 지닌 라프라스입니다. 겉보기엔 온화하지만 속으로는 수많은 생각과 당곡고의 숨은 진리를 꿰뚫어 보고 있습니다."},
    "INTJ": {"name": "뮤츠", "title": "냉철한 전략가", "img": "150", "stats": [90, 100, 50], "desc": "학교라는 시스템을 완벽하게 분석하고 자신만의 학습 효율을 극대화하는 뮤츠입니다. 머릿속에는 완벽한 마스터플랜이 그려져 있습니다."},
    "ISTP": {"name": "잠만보", "title": "가성비의 신", "img": "143", "stats": [100, 85, 55], "desc": "쉬는 시간엔 늘 엎드려 자고 있지만, 막상 시험을 보면 점수가 엄청난 기적의 잠만보입니다! 최소한의 노력으로 최대의 효율을 뽑아내는 실용주의자죠."},
    "ISFP": {"name": "이브이", "title": "자유로운 영혼", "img": "133", "stats": [60, 60, 95], "desc": "어떤 무리에든 자연스럽게 녹아드는 유연한 매력의 이브이입니다. 남에게 강요하는 것을 싫어하고 평화로우며 감성적인 하루하루를 살아갑니다."},
    "INFP": {"name": "뮤", "title": "몽상가 예술가", "img": "151", "stats": [80, 80, 90], "desc": "창가 자리에 앉아 뭉게구름을 보며 상상의 나래를 펼치는 뮤입니다. 마음속에 깊고 넓은 감수성의 우주를 품고 있는 순수한 영혼입니다."},
    "INTP": {"name": "폴리곤", "title": "논리적 팩트폭격기", "img": "137", "stats": [70, 90, 40], "desc": "정보 교과 시간을 가장 좋아하는 지적 호기심 대마왕 폴리곤입니다! 흥미 있는 분야는 끝까지 파고드는 학구파지만, 관심 없는 과목은 과감히 놓아버립니다."},
    "ESTP": {"name": "리자몽", "title": "위풍당당 행동대장", "img": "6", "stats": [70, 100, 85], "desc": "체육대회 때 가장 빛나는 당신! 불꽃같은 에너지를 뿜어내는 리자몽입니다. 복잡하게 생각하기보다 일단 부딪혀보는 실전파 학생입니다."},
    "ESFP": {"name": "푸린", "title": "무대 위의 인싸", "img": "39", "stats": [85, 50, 100], "desc": "당곡고 축제와 장기자랑의 주인공은 바로 나! 노래와 춤을 사랑하는 푸린입니다. 소중한 분위기 메이커입니다."},
    "ENFP": {"name": "피카츄", "title": "인간 비타민", "img": "25", "stats": [60, 90, 100], "desc": "쉬는 시간마다 교실을 누비며 친구들에게 웃음을 주는 에너자이저 피카츄입니다! 특유의 번뜩이는 아이디어와 친화력을 자랑합니다."},
    "ENTP": {"name": "팬텀", "title": "재기발랄 악동", "img": "94", "stats": [65, 85, 80], "desc": "선생님의 농담을 가장 재치 있게 받아치는 반의 공식 장난꾸러기 팬텀입니다! 틀에 갇힌 것을 싫어하고 늘 새롭고 기발한 아이디어를 쏟아냅니다."},
    "ESTJ": {"name": "거북왕", "title": "든든한 학생회장", "img": "9", "stats": [90, 85, 75], "desc": "학급의 규칙과 질서를 수호하는 듬직한 거북왕입니다. 카리스마 있게 주도하고 진두지휘하는 전형적인 리더상입니다."},
    "ESFJ": {"name": "토게피", "title": "친화력 끝판왕", "img": "175", "stats": [75, 40, 100], "desc": "복도를 걸어가면 반의반은 다 아는 얼굴! 엄청난 사교성을 자랑합니다. 친구들의 기분 변화를 귀신같이 눈치채고 챙겨주는 평화의 상징입니다."},
    "ENFJ": {"name": "망나뇽", "title": "따뜻한 카리스마", "img": "149", "stats": [95, 90, 95], "desc": "부드럽지만 강인한 매력으로 사람들을 이끄는 망나뇽입니다. 당곡고 학생들의 멘토를 자처하며 올바른 길로 갈 수 있도록 응원합니다."},
    "ENTJ": {"name": "갸라도스", "title": "거침없는 불도저", "img": "130", "stats": [85, 100, 70], "desc": "목표를 정하면 거칠 것 없이 돌진하는 야망 가득한 갸라도스입니다. 추진력이 엄청나서 어떤 프로젝트든 성공시켜버리는 압도적 실력자입니다."}
}

# 5. 무작위 댄스 리스트 정의 (CSS클래스명, 댄스설명)
dance_list = [
    ("dance-bounce", "🎶 폴짝폴짝 바운스 🎶"),
    ("dance-shake-spin", "💫 빙글빙글 쉐이크 스핀 💫"),
    ("dance-pulse", "💗 두근두근 펄스 💗"),
    ("dance-swing", "👋 시계추처럼 스윙스윙 👋"),
    ("dance-jelly", "🍮 젤리처럼 꿀렁꿀렁 🍮")
]

# 6. UI 구성
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    mbti_types = sorted(list(pokemon_data.keys()))
    selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types, label_visibility="collapsed")
    st.write("")

    if st.button("🚀 우주로 몬스터볼 던지기 🚀"):
        with st.spinner('은하계 포켓몬 도감 검색 중...'):
            time.sleep(1.2)
            
        st.balloons()
        
        result = pokemon_data[selected_mbti]
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{result['img']}.png"
        
        # 버튼을 누를 때마다 5개의 춤 중에서 1개를 무작위로 뽑음!
        chosen_dance_class, dance_name = random.choice(dance_list)
        
        # 홀로그램 카드 시작
        st.markdown('<div class="holo-card">', unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='color: #0fa; margin:0;'>[ {selected_mbti} ]</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='color: #fff; margin:0; font-size: 2.5rem; text-shadow: 0 0 10px #ff00de;'>{result['title']} {result['name']}</h1>", unsafe_allow_html=True)
        st.markdown("<hr style='border:1px solid rgba(0, 255, 255, 0.3);'>", unsafe_allow_html=True)
        
        inner_col1, inner_col2 = st.columns([1, 1.2])
        
        with inner_col1:
            # 선택된 댄스 클래스를 HTML <img> 태그에 쏙 집어넣기!
            st.markdown(f'<img src="{img_url}" class="poke-img {chosen_dance_class}">', unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center; font-weight:bold; color:#0fa; margin-top:15px;'>{dance_name}</p>", unsafe_allow_html=True)
            
        with inner_col2:
            st.markdown("<br>", unsafe_allow_html=True)
            tab1, tab2 = st.tabs(["📊 스탯", "💡 정보"])
            
            with tab1:
                st.markdown("<span style='color: white;'>💖 학교생활 생존력 (HP)</span>", unsafe_allow_html=True)
                st.progress(result['stats'][0])
                st.markdown("<span style='color: white;'>⚔️ 학업/동아리 열정 (ATK)</span>", unsafe_allow_html=True)
                st.progress(result['stats'][1])
                st.markdown("<span style='color: white;'>✨ 친구 친화도 (CHARM)</span>", unsafe_allow_html=True)
                st.progress(result['stats'][2])
                
            with tab2:
                st.info(f"**강점:** {result['title']}\n\n**서식지:** 당곡고등학교\n\n**진화 조건:** 기말고사 종료 후")
                
        # 다크 테마에 맞춘 어두운 스토리 텍스트 박스
        st.markdown(f'<div class="story-text-dark">{result["desc"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
