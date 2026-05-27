import streamlit as st
import time

# 1. 페이지 설정 (넓은 화면, 깔끔한 레이아웃)
st.set_page_config(page_title="프리미엄 MBTI 포켓몬", page_icon="💎", layout="wide")

# 2. 고급스러운 글래스모피즘 & 애니메이션 CSS 적용
st.markdown("""
<style>
    /* 전체 배경을 은은하고 고급스러운 파스텔 톤이 천천히 움직이도록 설정 */
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

    /* 최신 트렌드: 글래스모피즘 (유리 질감) 카드 디자인 */
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

    /* 그라데이션 텍스트 (깔끔하면서도 화려함) */
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

    /* 둥둥 떠다니는 포켓몬 애니메이션 */
    .floating-img {
        display: block;
        margin: 0 auto;
        width: 100%;
        max-width: 350px;
        animation: float 4s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }

    /* 세련된 버튼 디자인 */
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
    
    /* 긴 텍스트를 위한 문단 스타일 */
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

# 4. 방대한 포켓몬 데이터 (상세한 설명 추가)
pokemon_data = {
    "ISTJ": {
        "name": "이상해씨", 
        "title": "원칙주의자 모범생",
        "desc": "한 번 정한 목표는 흔들림 없이 밀고 나가는 듬직한 이상해씨입니다. 당곡고에서 당신은 항상 필기가 완벽하고, 수행평가 기한을 절대 어기지 않는 철저한 모범생 스타일이에요! 조별 과제를 할 때 자료조사와 정리를 기가 막히게 해내어 친구들의 신뢰를 한 몸에 받습니다. 묵묵히 자신의 길을 가는 당신의 등 뒤에는 언제나 단단한 씨앗이 자라고 있어요.",
        "img": "1", "stats": [85, 70, 60]
    },
    "ENFP": {
        "name": "피카츄", 
        "title": "인간 비타민 ⚡",
        "desc": "쉬는 시간마다 교실을 누비며 친구들에게 웃음을 주는 에너자이저 피카츄입니다! 당곡고의 분위기 메이커인 당신은 호기심이 많고 새로운 동아리를 만들거나 축제 장기자랑에 나가는 것을 즐깁니다. 가끔 수업 시간에 딴생각을 하기도 하지만, 특유의 번뜩이는 아이디어와 친화력으로 모든 사람을 당신의 팬으로 만들어버리는 무서운 매력의 소유자입니다.",
        "img": "25", "stats": [60, 90, 100]
    },
    "INTJ": {
        "name": "뮤츠", 
        "title": "냉철한 전략가 🧠",
        "desc": "학교라는 시스템을 완벽하게 분석하고 자신만의 학습 효율을 극대화하는 뮤츠입니다. 겉보기엔 조금 차가워 보일 수 있지만, 사실 머릿속에는 당곡고를 넘어 미래의 진로까지 완벽한 마스터플랜이 그려져 있습니다. 남들이 벼락치기를 할 때, 당신은 이미 3주 전부터 계획된 스케줄에 따라 여유롭게 1등급을 쟁취하는 지독하고 멋진 완벽주의자입니다.",
        "img": "150", "stats": [90, 100, 50]
    },
    "ISFJ": {
        "name": "럭키", 
        "title": "다정한 수호천사 🥚",
        "desc": "친구들이 힘들 때 가장 먼저 다가가 조용히 위로를 건네는 럭키입니다. 당곡고에서 당신은 보건 선생님처럼 친구들의 멘탈을 챙겨주는 따뜻한 사람입니다. 튀는 것을 좋아하지 않지만, 반에서 당신이 없으면 교실 분위기가 삭막해질 정도로 당신의 존재감은 큽니다. 책임감이 강해 궂은일도 마다하지 않는 진정한 외유내강의 표본입니다.",
        "img": "113", "stats": [100, 30, 95]
    },
    "ESTP": {
        "name": "리자몽",
        "title": "위풍당당 행동대장 🔥",
        "desc": "체육대회 때 가장 빛나는 당신! 불꽃같은 에너지를 뿜어내는 리자몽입니다. 복잡하게 생각하기보다 일단 부딪혀보는 실전파 학생으로, 위기 상황에서 놀라운 순발력을 발휘합니다. 지루한 것은 딱 질색이라 가끔 선생님의 레이더망에 걸리기도 하지만, 미워할 수 없는 호탕함과 리더십으로 친구들을 몰고 다니는 당곡고의 인싸입니다.",
        "img": "6", "stats": [70, 100, 85]
    },
    "INFP": {
        "name": "뮤",
        "title": "몽상가 예술가 🌸",
        "desc": "창가 자리에 앉아 턱을 괴고 뭉게구름을 보며 상상의 나래를 펼치는 뮤입니다. 마음속에 깊고 넓은 감수성의 우주를 품고 있는 당신은 글쓰기나 미술, 음악 등에서 뛰어난 재능을 보이곤 합니다. 다툼을 싫어하고 모두가 평화롭기를 바라는 순수한 영혼으로, 당신이 쓰는 글이나 말 한마디는 친구들에게 깊은 감동과 힐링을 줍니다.",
        "img": "151", "stats": [80, 80, 90]
    }
    # 학생 스스로 나머지 10개의 MBTI를 채워보는 학습을 위해 일부러 6개만 상세히 작성했습니다!
    # 나머지 MBTI는 아래에 기본값으로 둡니다. 직접 스토리를 작성해 보세요.
}

# (기본값 채우기 - 학생이 직접 긴 글을 써보도록 유도)
default_mbtis = ["INFJ", "ISTP", "ISFP", "INTP", "ESFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
for mbti in default_mbtis:
    pokemon_data[mbti] = {
        "name": "메타몽",
        "title": "무한한 가능성",
        "desc": "아직 상세한 관찰 보고서가 작성되지 않았습니다. 메타몽처럼 어떤 모습으로든 변할 수 있는 무한한 가능성을 지닌 당곡고 학생이군요! 직접 코드를 수정하여 나만의 학교생활 스토리를 꽉꽉 채워보세요.",
        "img": "132", "stats": [50, 50, 50]
    }

# 5. UI 구성 (가운데 정렬을 위해 빈 컬럼 활용)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # 선택 상자
    mbti_types = sorted(list(pokemon_data.keys()))
    selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types, label_visibility="collapsed")
    st.write("")

    if st.button("내 영혼의 포켓몬 분석하기 🔍"):
        with st.spinner('심리 분석 및 포켓몬 도감 동기화 중...'):
            time.sleep(1.2)
            
        st.balloons()
        
        result = pokemon_data[selected_mbti]
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{result['img']}.png"
        
        # 글래스모피즘 카드 시작
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        # 제목 및 포켓몬 이름
        st.markdown(f"<h3 style='color: #555; margin:0;'>{selected_mbti}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='color: #2575fc; margin:0; font-size: 2.5rem;'>{result['title']} [{result['name']}]</h1>", unsafe_allow_html=True)
        
        st.markdown("<hr style='border:1px solid rgba(0,0,0,0.1);'>", unsafe_allow_html=True)
        
        # 내용 영역 (이미지와 스탯)
        inner_col1, inner_col2 = st.columns([1, 1.2])
        
        with inner_col1:
            # 둥둥 떠다니는 애니메이션이 적용된 이미지
            st.markdown(f'<img src="{img_url}" class="floating-img">', unsafe_allow_html=True)
            
        with inner_col2:
            st.markdown("<br>", unsafe_allow_html=True)
            # 스트림릿 탭 기능을 사용하여 깔끔하게 정보 분리
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
                
        # 긴 설명을 깔끔하게 담는 하단 스토리 박스
        st.markdown(f'<div class="story-text">{result["desc"]}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
