import streamlit as st
import time

# 1. 페이지 설정
st.set_page_config(page_title="프리미엄 MBTI 포켓몬", page_icon="💎", layout="wide")

# 2. 고급스러운 글래스모피즘 & 춤추는 애니메이션 CSS 적용
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(-45deg, #fbc2eb, #a6c1ee, #fdcbf1, #e6dee9);
        background-size: 300% 300%;
        animation: smoothBg 20s ease infinite;
    }
    @keyframes smoothBg {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 25px;
        padding: 40px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        text-align: center;
        margin-top: 20px;
    }

    .gradient-text {
        background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .sub-text {
        color: #555;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 600;
    }

    /* 🕺 신나게 춤추는 포켓몬 애니메이션 🕺 */
    .dancing-img {
        display: block;
        margin: 0 auto;
        width: 100%;
        max-width: 350px;
        animation: dance 0.6s ease-in-out infinite; 
    }
    
    @keyframes dance {
        0% { transform: translateY(0px) rotate(0deg); }
        25% { transform: translateY(-15px) rotate(-10deg); }
        50% { transform: translateY(0px) rotate(0deg); }
        75% { transform: translateY(-15px) rotate(10deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    div.stButton > button:first-child {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 30px;
        font-size: 1.5rem;
        font-weight: bold;
        border: none;
        padding: 15px 0;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .story-text {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #333;
        text-align: left;
        background: rgba(255, 255, 255, 0.6);
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
        border-left: 5px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# 3. 타이틀 영역
st.markdown('<div class="gradient-text">✨ 프리미엄 MBTI 포켓몬 진단 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">당곡고등학교 학생들을 위한 맞춤형 심리 분석 도감 📖</div>', unsafe_allow_html=True)

# 4. 방대한 포켓몬 데이터 (16개 전체 채움!)
pokemon_data = {
    "ISTJ": {"name": "이상해씨", "title": "원칙주의자 모범생", "img": "1", "stats": [85, 70, 60],
             "desc": "한 번 정한 목표는 흔들림 없이 밀고 나가는 듬직한 이상해씨입니다. 당곡고에서 당신은 항상 필기가 완벽하고, 수행평가 기한을 절대 어기지 않는 철저한 모범생 스타일이에요! 조별 과제를 할 때 자료조사와 정리를 기가 막히게 해내어 친구들의 신뢰를 한 몸에 받습니다."},
    "ISFJ": {"name": "럭키", "title": "다정한 수호천사", "img": "113", "stats": [100, 30, 95],
             "desc": "친구들이 힘들 때 가장 먼저 다가가 조용히 위로를 건네는 럭키입니다. 당곡고에서 당신은 보건 선생님처럼 친구들의 멘탈을 챙겨주는 따뜻한 사람입니다. 튀는 것을 좋아하지 않지만, 반에서 당신이 없으면 교실 분위기가 삭막해질 정도로 당신의 존재감은 큽니다."},
    "INFJ": {"name": "라프라스", "title": "심연의 통찰가", "img": "131", "stats": [80, 60, 90],
             "desc": "조용하지만 날카로운 통찰력을 지닌 라프라스입니다. 겉보기엔 온화하지만 속으로는 수많은 생각과 당곡고의 숨은 진리를 꿰뚫어 보고 있습니다. 친구들의 깊은 고민을 가장 잘 들어주는 훌륭한 상담가이기도 합니다."},
    "INTJ": {"name": "뮤츠", "title": "냉철한 전략가", "img": "150", "stats": [90, 100, 50],
             "desc": "학교라는 시스템을 완벽하게 분석하고 자신만의 학습 효율을 극대화하는 뮤츠입니다. 겉보기엔 조금 차가워 보일 수 있지만, 사실 머릿속에는 완벽한 마스터플랜이 그려져 있습니다. 남들이 벼락치기를 할 때, 당신은 여유롭게 1등급을 쟁취합니다."},
    "ISTP": {"name": "잠만보", "title": "가성비의 신", "img": "143", "stats": [100, 85, 55],
             "desc": "쉬는 시간엔 늘 엎드려 자고 있지만, 막상 시험을 보면 점수가 엄청난 기적의 잠만보입니다! 최소한의 노력으로 최대의 효율을 뽑아내는 실용주의자죠. 복잡한 학교 행사보다는 조용히 혼자만의 시간을 갖는 것을 사랑합니다."},
    "ISFP": {"name": "이브이", "title": "자유로운 영혼", "img": "133", "stats": [60, 60, 95],
             "desc": "어떤 무리에든 자연스럽게 녹아드는 유연한 매력의 이브이입니다. 당곡고에서 미술이나 음악 등 예술적 감각이 가장 뛰어날 확률이 높습니다! 남에게 강요하는 것을 싫어하고 평화로우며 감성적인 하루하루를 살아갑니다."},
    "INFP": {"name": "뮤", "title": "몽상가 예술가", "img": "151", "stats": [80, 80, 90],
             "desc": "창가 자리에 앉아 뭉게구름을 보며 상상의 나래를 펼치는 뮤입니다. 마음속에 깊고 넓은 감수성의 우주를 품고 있는 당신은 뛰어난 문학적 재능을 보이곤 합니다. 순수한 영혼으로, 당신이 쓰는 글이나 말은 친구들에게 깊은 힐링을 줍니다."},
    "INTP": {"name": "폴리곤", "title": "논리적 팩트폭격기", "img": "137", "stats": [70, 90, 40],
             "desc": "정보 교과 시간을 가장 좋아하는 지적 호기심 대마왕 폴리곤입니다! 흥미 있는 분야는 끝까지 파고드는 학구파지만, 관심 없는 과목은 과감히 놓아버리기도 합니다. 가끔 뼈 때리는 팩트폭격으로 친구들을 놀라게 하지만 그만큼 솔직한 매력이 있습니다."},
    "ESTP": {"name": "리자몽", "title": "위풍당당 행동대장", "img": "6", "stats": [70, 100, 85],
             "desc": "체육대회 때 가장 빛나는 당신! 불꽃같은 에너지를 뿜어내는 리자몽입니다. 복잡하게 생각하기보다 일단 부딪혀보는 실전파 학생으로, 위기 상황에서 놀라운 순발력을 발휘합니다. 호탕함과 리더십으로 친구들을 몰고 다니는 당곡고의 인싸입니다."},
    "ESFP": {"name": "푸린", "title": "무대 위의 인싸", "img": "39", "stats": [85, 50, 100],
             "desc": "당곡고 축제와 장기자랑의 주인공은 바로 나! 노래와 춤, 노는 것을 사랑하는 푸린입니다. 당신 주변에는 항상 웃음이 끊이지 않으며, 교실의 공기가 무겁게 가라앉았을 때 분위기를 확 띄워주는 소중한 분위기 메이커입니다."},
    "ENFP": {"name": "피카츄", "title": "인간 비타민", "img": "25", "stats": [60, 90, 100],
             "desc": "쉬는 시간마다 교실을 누비며 친구들에게 웃음을 주는 에너자이저 피카츄입니다! 호기심이 많아 새로운 동아리를 만들거나 행사를 기획하는 것을 즐깁니다. 특유의 번뜩이는 아이디어와 친화력으로 모든 사람을 당신의 팬으로 만들어버립니다."},
    "ENTP": {"name": "팬텀", "title": "재기발랄 악동", "img": "94", "stats": [65, 85, 80],
             "desc": "선생님의 농담을 가장 재치 있게 받아치는 반의 공식 장난꾸러기 팬텀입니다! 틀에 갇힌 것을 싫어하고 늘 새롭고 기발한 아이디어를 쏟아냅니다. 토론을 좋아해서 가끔 말싸움에서 절대 지지 않는 무서운 달변가이기도 합니다."},
    "ESTJ": {"name": "거북왕", "title": "든든한 학생회장", "img": "9", "stats": [90, 85, 75],
             "desc": "학급의 규칙과 질서를 수호하는 듬직한 거북왕입니다. 카리스마 있게 조별 과제를 주도하고, 모두가 역할을 다할 수 있도록 진두지휘하는 전형적인 리더상입니다. 선생님들이 가장 믿고 일을 맡기는 당곡고의 핵심 인재입니다!"},
    "ESFJ": {"name": "토게피", "title": "친화력 끝판왕", "img": "175", "stats": [75, 40, 100],
             "desc": "복도를 걸어가면 반의반은 다 아는 얼굴! 엄청난 사교성과 오지랖을 자랑하는 토게피입니다. 친구들의 기분 변화를 귀신같이 눈치채고 챙겨주며, 갈등이 생기면 중간에서 완벽한 중재자 역할을 하는 평화의 상징입니다."},
    "ENFJ": {"name": "망나뇽", "title": "따뜻한 카리스마", "img": "149", "stats": [95, 90, 95],
             "desc": "부드럽지만 강인한 매력으로 사람들을 이끄는 망나뇽입니다. 당곡고 학생들의 멘토를 자처하며, 친구들이 올바른 길로 갈 수 있도록 응원과 격려를 아끼지 않습니다. 말과 행동에서 신뢰감이 뚝뚝 묻어나는 다정한 리더입니다."},
    "ENTJ": {"name": "갸라도스", "title": "거침없는 불도저", "img": "130", "stats": [85, 100, 70],
             "desc": "목표를 정하면 거칠 것 없이 돌진하는 야망 가득한 갸라도스입니다. 당곡고에서 가장 체계적이고 큰 목표를 가지고 있으며, 추진력이 엄청나서 어떤 프로젝트든 성공시켜버립니다. 다소 직설적이지만 그만큼 능력으로 증명하는 압도적 실력자입니다."}
}

# 5. UI 구성
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    mbti_types = sorted(list(pokemon_data.keys()))
    selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types, label_visibility="collapsed")
    st.write("")

    if st.button("내 영혼의 포켓몬 분석하기 🔍"):
        with st.spinner('심리 분석 및 포켓몬 도감 동기화 중...'):
            time.sleep(1.2)
            
        st.balloons()
        
        result = pokemon_data[selected_mbti]
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{result['img']}.png"
        
        # 글래스모피즘 카드
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        st.markdown(f"<h3 style='color: #555; margin:0;'>{selected_mbti}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='color: #2575fc; margin:0; font-size: 2.5rem;'>{result['title']} [{result['name']}]</h1>", unsafe_allow_html=True)
        st.markdown("<hr style='border:1px solid rgba(0,0,0,0.1);'>", unsafe_allow_html=True)
        
        inner_col1, inner_col2 = st.columns([1, 1.2])
        
        with inner_col1:
            # 💃 춤추는 애니메이션 클래스(dancing-img) 유지! 🕺
            st.markdown(f'<img src="{img_url}" class="dancing-img">', unsafe_allow_html=True)
            st.markdown("<p style='text-align:center; font-weight:bold; color:#ff00de; margin-top:10px;'>🎶 둠칫 둠칫 🎶</p>", unsafe_allow_html=True)
            
        with inner_col2:
            st.markdown("<br>", unsafe_allow_html=True)
            tab1, tab2 = st.tabs(["📊 능력치 분석", "💡 특징 요약"])
            
            with tab1:
                st.caption("💖 학교생활 생존력 (HP)")
                st.progress(result['stats'][0])
                st.caption("⚔️ 학업/동아리 열정 (ATK)")
                st.progress(result['stats'][1])
                st.caption("✨ 친구 친화도 (CHARM)")
                st.progress(result['stats'][2])
                
            with tab2:
                st.info(f"**강점:** {result['title']}다운 면모\n\n**서식지:** 당곡고등학교 교실 어딘가\n\n**진화 조건:** 기말고사 종료 후")
                
        st.markdown(f'<div class="story-text">{result["desc"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
