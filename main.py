import streamlit as st
import time
import random

# 1. 페이지 설정
st.set_page_config(page_title="당곡고 포켓몬 도감 & 배틀", page_icon="🌌", layout="wide")

# 2. 게임 상태(Session State) 초기화 세팅
if 'my_mbti' not in st.session_state:
    st.session_state.my_mbti = None
if 'dance_class' not in st.session_state:
    st.session_state.dance_class = ""
if 'dance_name' not in st.session_state:
    st.session_state.dance_name = ""
if 'battle_active' not in st.session_state:
    st.session_state.battle_active = False
if 'battle_log' not in st.session_state:
    st.session_state.battle_log = []
if 'my_hp' not in st.session_state:
    st.session_state.my_hp = 0
if 'opp_hp' not in st.session_state:
    st.session_state.opp_hp = 0

# 3. 우주 테마 & 시인성 개선 CSS 적용 ★★★
st.markdown("""
<style>
    /* 우주 배경 */
    .stApp {
        background: linear-gradient(270deg, #11052C, #3D087B, #270082, #000000);
        background-size: 800% 800%;
        animation: cosmicBg 15s ease infinite;
        color: white;
    }
    @keyframes cosmicBg { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }

    /* 텍스트 스타일 */
    .neon-text { color: #fff; text-shadow: 0 0 10px #fff, 0 0 20px #0fa, 0 0 40px #0fa; font-size: 3.5rem; font-weight: 900; text-align: center; margin-bottom: 5px; }
    .sub-text { color: #0fa; font-size: 1.2rem; text-align: center; margin-bottom: 40px; font-weight: bold; }

    /* 도감 카드 (홀로그램 효과) */
    .holo-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
        backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 255, 255, 0.5); border-radius: 20px; padding: 40px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.4); text-align: center; margin-top: 20px;
    }
    
    /* 배틀용 미니 카드 */
    .battle-card {
        background: rgba(0, 0, 0, 0.5); border: 2px solid #0fa; border-radius: 15px; padding: 20px; text-align: center;
    }

    .poke-img { display: block; margin: 0 auto; width: 100%; max-width: 300px; filter: drop-shadow(0px 0px 20px rgba(255, 255, 255, 0.6)); }
    .battle-img { max-width: 200px; }
    
    .vs-text { font-size: 4rem; font-weight: 900; color: #ff004c; text-shadow: 0 0 20px #ff004c; text-align: center; margin-top: 40%; }

    /* 무작위 댄스 애니메이션 */
    @keyframes bounce { 0%, 100% { transform: translateY(0) scale(1); } 50% { transform: translateY(-25px) scale(1.05); } }
    .dance-bounce { animation: bounce 0.5s ease-in-out infinite; }
    @keyframes shake-spin { 0% { transform: rotate(0deg); } 25% { transform: rotate(15deg); } 50% { transform: rotate(0deg); } 75% { transform: rotate(-15deg); } 100% { transform: rotate(360deg); } }
    .dance-shake-spin { animation: shake-spin 1s linear infinite; }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.2) rotate(5deg); } }
    .dance-pulse { animation: pulse 0.6s ease-in-out infinite; }
    @keyframes swing { 0%, 100% { transform: rotate(0deg); transform-origin: top center; } 33% { transform: rotate(15deg); } 66% { transform: rotate(-15deg); } }
    .dance-swing { animation: swing 0.8s ease-in-out infinite; }
    @keyframes jelly { 0%, 100% { transform: scale(1, 1); } 25% { transform: scale(1.15, 0.85); } 50% { transform: scale(0.85, 1.15); } 75% { transform: scale(1.05, 0.95); } }
    .dance-jelly { animation: jelly 0.7s infinite; }

    /* 전투 로그 및 설명 박스 */
    .battle-log-box {
        background: rgba(0,0,0,0.8); border-left: 5px solid #0fa; padding: 15px; border-radius: 10px;
        font-family: 'Courier New', Courier, monospace; height: 180px; overflow-y: auto; margin-top: 10px; color: white;
    }
    .story-text-dark {
        font-size: 1.1rem; line-height: 1.8; color: #ffffff; text-align: left; background: rgba(0, 0, 0, 0.7);
        padding: 20px; border-radius: 15px; margin-top: 20px; border-left: 5px solid #0fa;
    }

    /* ========================================================
       🚨 스트림릿 기본 위젯(입력창) 가독성 해결을 위한 CSS 추가 부분 
       ======================================================== */
       
    /* 1. 선택 상자(Selectbox) 디자인: 배경색과 글자색 대비 확실하게 */
    div[data-baseweb="select"] > div {
        background-color: #1a1a2e !important;
        color: #ffffff !important;
        border: 2px solid #0fa !important;
        border-radius: 10px !important;
    }
    
    /* 2. 드롭다운 메뉴(클릭 시 나오는 목록) 디자인 */
    ul[data-baseweb="menu"] {
        background-color: #1a1a2e !important;
    }
    ul[data-baseweb="menu"] li {
        color: #ffffff !important;
    }

    /* 3. 선택상자 위의 라벨(안내 문구) 색상 지정 */
    div.stSelectbox label {
        color: #0fa !important;
        font-weight: 900 !important;
        font-size: 1.1rem !important;
    }

    /* 4. 정보/알림창 (st.info, st.error 등) 글자색 지정 */
    div[data-testid="stAlert"] {
        background-color: rgba(0, 0, 0, 0.6) !important;
        border: 1px solid #0fa !important;
    }
    div[data-testid="stAlert"] p {
        color: #ffffff !important;
    }
    
    /* 5. 탭(st.tabs) 제목 글자색 지정 */
    button[data-baseweb="tab"] {
        color: #aaaaaa !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #0fa !important;
        font-weight: bold !important;
    }
    
    /* 6. 프로그레스 바 텍스트 색상 강제 지정 */
    div[data-testid="stProgressBar"] label {
        color: #ffffff !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# 4. 포켓몬 데이터
pokemon_data = {
    "ISTJ": {"name": "이상해씨", "title": "원칙주의자 모범생", "img": "1", "hp": 150, "atk": 40, "charm": 60, "desc": "한 번 정한 목표는 흔들림 없이 밀고 나가는 듬직한 이상해씨입니다. 당곡고에서 당신은 항상 필기가 완벽하고, 수행평가 기한을 절대 어기지 않는 철저한 모범생 스타일이에요!"},
    "ISFJ": {"name": "럭키", "title": "다정한 수호천사", "img": "113", "hp": 200, "atk": 25, "charm": 95, "desc": "친구들이 힘들 때 가장 먼저 다가가 조용히 위로를 건네는 럭키입니다. 반에서 당신이 없으면 교실 분위기가 삭막해질 정도로 당신의 존재감은 큽니다."},
    "INFJ": {"name": "라프라스", "title": "심연의 통찰가", "img": "131", "hp": 160, "atk": 45, "charm": 90, "desc": "조용하지만 날카로운 통찰력을 지닌 라프라스입니다. 겉보기엔 온화하지만 속으로는 수많은 생각과 당곡고의 숨은 진리를 꿰뚫어 보고 있습니다."},
    "INTJ": {"name": "뮤츠", "title": "냉철한 전략가", "img": "150", "hp": 140, "atk": 65, "charm": 50, "desc": "학교라는 시스템을 완벽하게 분석하고 자신만의 학습 효율을 극대화하는 뮤츠입니다. 머릿속에는 완벽한 마스터플랜이 그려져 있습니다."},
    "ISTP": {"name": "잠만보", "title": "가성비의 신", "img": "143", "hp": 220, "atk": 50, "charm": 55, "desc": "쉬는 시간엔 늘 엎드려 자고 있지만, 막상 시험을 보면 점수가 엄청난 기적의 잠만보입니다! 최소한의 노력으로 최대의 효율을 뽑아내는 실용주의자죠."},
    "ISFP": {"name": "이브이", "title": "자유로운 영혼", "img": "133", "hp": 130, "atk": 35, "charm": 95, "desc": "어떤 무리에든 자연스럽게 녹아드는 유연한 매력의 이브이입니다. 남에게 강요하는 것을 싫어하고 평화로우며 감성적인 하루하루를 살아갑니다."},
    "INFP": {"name": "뮤", "title": "몽상가 예술가", "img": "151", "hp": 140, "atk": 55, "charm": 90, "desc": "창가 자리에 앉아 뭉게구름을 보며 상상의 나래를 펼치는 뮤입니다. 마음속에 깊고 넓은 감수성의 우주를 품고 있는 순수한 영혼입니다."},
    "INTP": {"name": "폴리곤", "title": "논리적 팩트폭격기", "img": "137", "hp": 135, "atk": 60, "charm": 40, "desc": "정보 교과 시간을 가장 좋아하는 지적 호기심 대마왕 폴리곤입니다! 흥미 있는 분야는 끝까지 파고드는 학구파지만, 관심 없는 과목은 과감히 놓아버립니다."},
    "ESTP": {"name": "리자몽", "title": "위풍당당 행동대장", "img": "6", "hp": 145, "atk": 70, "charm": 85, "desc": "체육대회 때 가장 빛나는 당신! 불꽃같은 에너지를 뿜어내는 리자몽입니다. 복잡하게 생각하기보다 일단 부딪혀보는 실전파 학생입니다."},
    "ESFP": {"name": "푸린", "title": "무대 위의 인싸", "img": "39", "hp": 170, "atk": 30, "charm": 100, "desc": "당곡고 축제와 장기자랑의 주인공은 바로 나! 노래와 춤을 사랑하는 푸린입니다. 소중한 분위기 메이커입니다."},
    "ENFP": {"name": "피카츄", "title": "인간 비타민", "img": "25", "hp": 120, "atk": 55, "charm": 100, "desc": "쉬는 시간마다 교실을 누비며 친구들에게 웃음을 주는 에너자이저 피카츄입니다! 특유의 번뜩이는 아이디어와 친화력을 자랑합니다."},
    "ENTP": {"name": "팬텀", "title": "재기발랄 악동", "img": "94", "hp": 125, "atk": 65, "charm": 80, "desc": "선생님의 농담을 가장 재치 있게 받아치는 반의 공식 장난꾸러기 팬텀입니다! 틀에 갇힌 것을 싫어하고 늘 새롭고 기발한 아이디어를 쏟아냅니다."},
    "ESTJ": {"name": "거북왕", "title": "든든한 학생회장", "img": "9", "hp": 165, "atk": 50, "charm": 75, "desc": "학급의 규칙과 질서를 수호하는 듬직한 거북왕입니다. 카리스마 있게 주도하고 진두지휘하는 전형적인 리더상입니다."},
    "ESFJ": {"name": "토게피", "title": "친화력 끝판왕", "img": "175", "hp": 140, "atk": 20, "charm": 100, "desc": "복도를 걸어가면 반의반은 다 아는 얼굴! 엄청난 사교성을 자랑합니다. 친구들의 기분 변화를 귀신같이 눈치채고 챙겨주는 평화의 상징입니다."},
    "ENFJ": {"name": "망나뇽", "title": "따뜻한 카리스마", "img": "149", "hp": 155, "atk": 65, "charm": 95, "desc": "부드럽지만 강인한 매력으로 사람들을 이끄는 망나뇽입니다. 당곡고 학생들의 멘토를 자처하며 올바른 길로 갈 수 있도록 응원합니다."},
    "ENTJ": {"name": "갸라도스", "title": "거침없는 불도저", "img": "130", "hp": 150, "atk": 75, "charm": 70, "desc": "목표를 정하면 거칠 것 없이 돌진하는 야망 가득한 갸라도스입니다. 추진력이 엄청나서 어떤 프로젝트든 성공시켜버리는 압도적 실력자입니다."}
}

dance_list = [
    ("dance-bounce", "🎶 폴짝폴짝 바운스 🎶"),
    ("dance-shake-spin", "💫 빙글빙글 쉐이크 스핀 💫"),
    ("dance-pulse", "💗 두근두근 펄스 💗"),
    ("dance-swing", "👋 시계추처럼 스윙스윙 👋"),
    ("dance-jelly", "🍮 젤리처럼 꿀렁꿀렁 🍮")
]

mbti_types = sorted(list(pokemon_data.keys()))

# ==========================================
# 🌠 [섹션 1] 포켓몬 도감 검색부
# ==========================================
st.markdown('<div class="neon-text">🌌 은하계 MBTI 포켓몬 🌌</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">내 포켓몬을 소환하고 스크롤을 내려 배틀을 진행하세요! 👇</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_mbti = st.selectbox("👇 당신의 MBTI를 선택하세요", mbti_types)
    
    if st.button("🚀 내 포켓몬 소환하기!", use_container_width=True):
        st.session_state.my_mbti = selected_mbti
        st.session_state.dance_class, st.session_state.dance_name = random.choice(dance_list)
        st.session_state.battle_active = False 
        st.balloons()

# 도감 결과 출력부
if st.session_state.my_mbti:
    my_poke = pokemon_data[st.session_state.my_mbti]
    img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{my_poke['img']}.png"
    
    with col2:
        st.markdown('<div class="holo-card">', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: #0fa; margin:0;'>[ {st.session_state.my_mbti} ]</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='color: #fff; margin:0; text-shadow: 0 0 10px #ff00de;'>{my_poke['title']} {my_poke['name']}</h1>", unsafe_allow_html=True)
        
        st.markdown(f'<img src="{img_url}" class="poke-img {st.session_state.dance_class}">', unsafe_allow_html=True)
        st.markdown(f"<p style='color:#0fa; font-weight:bold;'>{st.session_state.dance_name}</p>", unsafe_allow_html=True)
        
        # 탭을 활용하여 스탯과 정보를 분리
        tab1, tab2 = st.tabs(["📊 상세 능력치", "💡 특징 및 서식지"])
        with tab1:
            st.write("")
            st.progress(my_poke['hp'] / 250, text=f"💖 체력 (HP): {my_poke['hp']}")
            st.progress(my_poke['atk'] / 100, text=f"⚔️ 공격력 (ATK): {my_poke['atk']}")
            st.progress(my_poke['charm'] / 100, text=f"✨ 매력 (CHARM): {my_poke['charm']}")
        with tab2:
            st.info(f"✅ **장점:** {my_poke['title']}\n\n🏫 **서식지:** 당곡고등학교 내 어딘가\n\n🌟 **진화조건:** 기말고사 종료 후")
        
        st.markdown(f'<div class="story-text-dark">{my_poke["desc"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("---") 

    # ==========================================
    # ⚔️ [섹션 2] 배틀 아레나
    # ==========================================
    st.markdown('<div class="neon-text" style="font-size: 2.5rem;">⚔️ 지하 배틀 아레나 ⚔️</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text" style="color: #ff004c;">다른 MBTI의 포켓몬과 승부를 겨뤄보세요!</div>', unsafe_allow_html=True)

    col_set1, col_set2 = st.columns(2)
    with col_set1:
        st.info(f"🟢 **나의 포켓몬:** {st.session_state.my_mbti} [{my_poke['name']}] (HP: {my_poke['hp']})")
    with col_set2:
        opp_mbti = st.selectbox("🔴 배틀할 상대방 MBTI 선택", mbti_types, key="opp_select")
        
    if st.button("🔥 이 상대와 배틀 시작! 🔥", use_container_width=True):
        st.session_state.opp_mbti = opp_mbti
        st.session_state.battle_active = True
        st.session_state.my_hp = my_poke['hp']
        st.session_state.my_max_hp = my_poke['hp']
        st.session_state.opp_hp = pokemon_data[opp_mbti]['hp']
        st.session_state.opp_max_hp = pokemon_data[opp_mbti]['hp']
        st.session_state.battle_log = [f"📢 야생의 {opp_mbti} [{pokemon_data[opp_mbti]['name']}]이(가) 승부를 걸어왔다!"]
    
    if st.session_state.battle_active:
        opp_poke = pokemon_data[st.session_state.opp_mbti]
        
        b_col1, b_col2, b_col3 = st.columns([2, 1, 2])
        
        with b_col1:
            st.markdown('<div class="battle-card">', unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:white;'>{st.session_state.my_mbti} [{my_poke['name']}]</h3>", unsafe_allow_html=True)
            
            my_hp_ratio = max(0.0, min(1.0, st.session_state.my_hp / st.session_state.my_max_hp))
            st.progress(my_hp_ratio, text=f"HP: {max(0, st.session_state.my_hp)} / {st.session_state.my_max_hp}")
            
            if st.session_state.my_hp <= 0:
                st.markdown(f'<img src="{img_url}" class="poke-img battle-img" style="filter: grayscale(100%); transform: rotate(90deg);">', unsafe_allow_html=True)
            else:
                st.markdown(f'<img src="{img_url}" class="poke-img battle-img dance-bounce">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with b_col2:
            st.markdown('<div class="vs-text">VS</div>', unsafe_allow_html=True)
            
        with b_col3:
            st.markdown('<div class="battle-card" style="border-color: #ff004c;">', unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:white;'>{st.session_state.opp_mbti} [{opp_poke['name']}]</h3>", unsafe_allow_html=True)
            
            opp_img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{opp_poke['img']}.png"
            opp_hp_ratio = max(0.0, min(1.0, st.session_state.opp_hp / st.session_state.opp_max_hp))
            st.progress(opp_hp_ratio, text=f"HP: {max(0, st.session_state.opp_hp)} / {st.session_state.opp_max_hp}")
            
            if st.session_state.opp_hp <= 0:
                st.markdown(f'<img src="{opp_img_url}" class="poke-img battle-img" style="filter: grayscale(100%); transform: rotate(-90deg);">', unsafe_allow_html=True)
            else:
                st.markdown(f'<img src="{opp_img_url}" class="poke-img battle-img dance-swing">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)
        if st.session_state.my_hp > 0 and st.session_state.opp_hp > 0:
            if st.button("⚡ 가라! 공격하기! ⚡", use_container_width=True):
                my_dmg = int(my_poke['atk'] * random.uniform(0.8, 1.2))
                st.session_state.opp_hp -= my_dmg
                st.session_state.battle_log.append(f"🔵 {my_poke['name']}의 공격! 상대에게 {my_dmg}의 피해!")
                
                if st.session_state.opp_hp > 0:
                    opp_dmg = int(opp_poke['atk'] * random.uniform(0.8, 1.2))
                    st.session_state.my_hp -= opp_dmg
                    st.session_state.battle_log.append(f"🔴 {opp_poke['name']}의 반격! 나에게 {opp_dmg}의 피해!")
                
                if st.session_state.opp_hp <= 0:
                    st.session_state.battle_log.append(f"🏆 {opp_poke['name']}이(가) 쓰러졌다! 당곡고 최고의 포켓몬 마스터 등극!")
                    st.balloons()
                elif st.session_state.my_hp <= 0:
                    st.session_state.battle_log.append(f"💀 {my_poke['name']}이(가) 쓰러졌다... 눈앞이 깜깜해졌다.")
                
                st.rerun()

        else:
            st.error("배틀이 종료되었습니다!")
            
        log_html = "<div class='battle-log-box'>"
        for log in reversed(st.session_state.battle_log):
            log_html += f"<p>{log}</p>"
        log_html += "</div>"
        st.markdown(log_html, unsafe_allow_html=True)
