import streamlit as st
import time
import random

# 1. 페이지 설정
st.set_page_config(page_title="당곡고 포켓몬 배틀", page_icon="⚔️", layout="wide")

# 2. 게임 상태(Session State) 초기화 세팅 ★★★ (매우 중요!)
# 스트림릿이 체력과 배틀 상황을 까먹지 않도록 기억창고에 저장하는 과정입니다.
if 'game_mode' not in st.session_state:
    st.session_state.game_mode = 'select' # 'select'(선택창) 또는 'battle'(배틀창)
if 'battle_log' not in st.session_state:
    st.session_state.battle_log = []
if 'my_hp' not in st.session_state:
    st.session_state.my_hp = 100
if 'opp_hp' not in st.session_state:
    st.session_state.opp_hp = 100

# 3. 우주 테마 & 애니메이션 CSS
st.markdown("""
<style>
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
    .neon-text {
        color: #fff;
        text-shadow: 0 0 10px #fff, 0 0 20px #0fa, 0 0 40px #0fa;
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }
    .holo-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 2px solid rgba(0, 255, 255, 0.5);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.4);
        text-align: center;
    }
    .poke-img {
        display: block;
        margin: 0 auto;
        width: 100%;
        max-width: 250px;
        filter: drop-shadow(0px 0px 20px rgba(255, 255, 255, 0.6));
    }
    .vs-text {
        font-size: 5rem;
        font-weight: 900;
        color: #ff004c;
        text-shadow: 0 0 20px #ff004c, 0 0 40px #ff0000;
        text-align: center;
        margin-top: 50%;
    }
    /* 춤추는 애니메이션 */
    @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
    .dance-bounce { animation: bounce 0.5s infinite; }
    
    @keyframes swing { 0%, 100% { transform: rotate(0deg); } 50% { transform: rotate(15deg); } }
    .dance-swing { animation: swing 0.6s infinite; }
    
    .battle-log-box {
        background: rgba(0,0,0,0.7);
        border-left: 5px solid #0fa;
        padding: 15px;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        height: 200px;
        overflow-y: auto;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 4. 방대한 포켓몬 데이터
pokemon_data = {
    "ISTJ": {"name": "이상해씨", "img": "1", "hp": 150, "atk": 40},
    "ISFJ": {"name": "럭키", "img": "113", "hp": 200, "atk": 25},
    "INFJ": {"name": "라프라스", "img": "131", "hp": 160, "atk": 45},
    "INTJ": {"name": "뮤츠", "img": "150", "hp": 140, "atk": 65},
    "ISTP": {"name": "잠만보", "img": "143", "hp": 220, "atk": 50},
    "ISFP": {"name": "이브이", "img": "133", "hp": 130, "atk": 35},
    "INFP": {"name": "뮤", "img": "151", "hp": 140, "atk": 55},
    "INTP": {"name": "폴리곤", "img": "137", "hp": 135, "atk": 60},
    "ESTP": {"name": "리자몽", "img": "6", "hp": 145, "atk": 70},
    "ESFP": {"name": "푸린", "img": "39", "hp": 170, "atk": 30},
    "ENFP": {"name": "피카츄", "img": "25", "hp": 120, "atk": 55},
    "ENTP": {"name": "팬텀", "img": "94", "hp": 125, "atk": 65},
    "ESTJ": {"name": "거북왕", "img": "9", "hp": 165, "atk": 50},
    "ESFJ": {"name": "토게피", "img": "175", "hp": 140, "atk": 20},
    "ENFJ": {"name": "망나뇽", "img": "149", "hp": 155, "atk": 65},
    "ENTJ": {"name": "갸라도스", "img": "130", "hp": 150, "atk": 75}
}

mbti_types = sorted(list(pokemon_data.keys()))

st.markdown('<div class="neon-text">⚔️ 당곡고 MBTI 배틀 아레나 ⚔️</div>', unsafe_allow_html=True)

# ==========================================
# 🎮 [모드 1] 포켓몬 선택 화면
# ==========================================
if st.session_state.game_mode == 'select':
    st.markdown("<h3 style='text-align:center; color:#0fa;'>나와 상대방의 MBTI를 골라주세요!</h3>", unsafe_allow_html=True)
    
    col_my, col_vs, col_opp = st.columns([2, 1, 2])
    
    with col_my:
        st.markdown("<h2 style='text-align:center; color:#fff;'>나의 MBTI</h2>", unsafe_allow_html=True)
        my_mbti = st.selectbox("내 MBTI", mbti_types, key="my_sel", label_visibility="collapsed")
        my_poke = pokemon_data[my_mbti]
        st.image(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{my_poke['img']}.png", use_column_width=True)
        
    with col_vs:
        st.markdown('<div class="vs-text">VS</div>', unsafe_allow_html=True)
        
    with col_opp:
        st.markdown("<h2 style='text-align:center; color:#fff;'>상대방 MBTI</h2>", unsafe_allow_html=True)
        # 내 MBTI와 다른 것을 기본값으로 설정하기 위한 처리
        opp_default_idx = 1 if my_mbti == mbti_types[0] else 0
        opp_mbti = st.selectbox("상대 MBTI", mbti_types, index=opp_default_idx, key="opp_sel", label_visibility="collapsed")
        opp_poke = pokemon_data[opp_mbti]
        st.image(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{opp_poke['img']}.png", use_column_width=True)

    st.write("")
    # 배틀 시작 버튼!
    if st.button("🔥 배틀 시작하기! 🔥", use_container_width=True):
        # 게임 상태를 배틀 모드로 변경하고, 체력과 정보를 세팅합니다.
        st.session_state.game_mode = 'battle'
        st.session_state.my_mbti = my_mbti
        st.session_state.opp_mbti = opp_mbti
        st.session_state.my_max_hp = my_poke['hp']
        st.session_state.opp_max_hp = opp_poke['hp']
        st.session_state.my_hp = my_poke['hp']
        st.session_state.opp_hp = opp_poke['hp']
        st.session_state.battle_log = [f"📢 야생의 당곡고 {opp_mbti}({opp_poke['name']})이(가) 승부를 걸어왔다!"]
        st.rerun() # 화면을 즉시 새로고침하여 배틀창으로 넘어감

# ==========================================
# 🎮 [모드 2] 본격적인 배틀 화면
# ==========================================
elif st.session_state.game_mode == 'battle':
    my_poke = pokemon_data[st.session_state.my_mbti]
    opp_poke = pokemon_data[st.session_state.opp_mbti]
    
    col_my, col_vs, col_opp = st.columns([2, 1, 2])
    
    # 🟢 내 포켓몬 UI
    with col_my:
        st.markdown('<div class="holo-card">', unsafe_allow_html=True)
        st.markdown(f"<h2>{st.session_state.my_mbti} [{my_poke['name']}]</h2>", unsafe_allow_html=True)
        # 내 체력바 (HP가 0 이하로 내려가지 않도록 max 처리)
        my_current_hp = max(0, st.session_state.my_hp)
        my_hp_ratio = my_current_hp / st.session_state.my_max_hp
        st.progress(my_hp_ratio, text=f"HP: {my_current_hp} / {st.session_state.my_max_hp}")
        
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{my_poke['img']}.png"
        
        # HP가 0이면 쓰러진 연출, 아니면 춤추기
        if my_current_hp == 0:
            st.markdown(f'<img src="{img_url}" class="poke-img" style="filter: grayscale(100%); transform: rotate(90deg);">', unsafe_allow_html=True)
        else:
            st.markdown(f'<img src="{img_url}" class="poke-img dance-bounce">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ⚡ VS 텍스트
    with col_vs:
        st.markdown('<div class="vs-text">VS</div>', unsafe_allow_html=True)

    # 🔴 상대 포켓몬 UI
    with col_opp:
        st.markdown('<div class="holo-card" style="border-color: #ff004c; box-shadow: 0 0 20px rgba(255, 0, 76, 0.4);">', unsafe_allow_html=True)
        st.markdown(f"<h2>{st.session_state.opp_mbti} [{opp_poke['name']}]</h2>", unsafe_allow_html=True)
        
        opp_current_hp = max(0, st.session_state.opp_hp)
        opp_hp_ratio = opp_current_hp / st.session_state.opp_max_hp
        st.progress(opp_hp_ratio, text=f"HP: {opp_current_hp} / {st.session_state.opp_max_hp}")
        
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{opp_poke['img']}.png"
        
        if opp_current_hp == 0:
            st.markdown(f'<img src="{img_url}" class="poke-img" style="filter: grayscale(100%); transform: rotate(90deg);">', unsafe_allow_html=True)
        else:
            st.markdown(f'<img src="{img_url}" class="poke-img dance-swing">', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 📝 전투 로그 출력창
    st.markdown("### 📜 전투 기록")
    log_html = "<div class='battle-log-box'>"
    for log in reversed(st.session_state.battle_log): # 최신 로그가 위로 오도록 뒤집음
        log_html += f"<p>{log}</p>"
    log_html += "</div>"
    st.markdown(log_html, unsafe_allow_html=True)

    st.write("")
    
    # ⚔️ 전투 액션 및 결과 판정
    if st.session_state.my_hp > 0 and st.session_state.opp_hp > 0:
        if st.button("⚔️ 수행평가의 분노로 공격하기! ⚔️", use_container_width=True):
            # 1. 내가 먼저 공격 (기본 공격력의 80~120% 사이의 무작위 데미지)
            my_dmg = int(my_poke['atk'] * random.uniform(0.8, 1.2))
            # 가끔 발생하는 치명타(크리티컬) 로직
            if random.random() < 0.2: # 20% 확률
                my_dmg = int(my_dmg * 1.5)
                st.session_state.battle_log.append(f"💥 [크리티컬!] {my_poke['name']}의 급소 찌르기! 상대에게 {my_dmg}의 엄청난 피해를 입혔다!")
            else:
                st.session_state.battle_log.append(f"🔵 {my_poke['name']}의 공격! 상대에게 {my_dmg}의 피해를 입혔다.")
            
            st.session_state.opp_hp -= my_dmg
            
            # 2. 상대가 살아있다면 반격
            if st.session_state.opp_hp > 0:
                opp_dmg = int(opp_poke['atk'] * random.uniform(0.8, 1.2))
                if random.random() < 0.2:
                    opp_dmg = int(opp_dmg * 1.5)
                    st.session_state.battle_log.append(f"💥 [크리티컬!] {opp_poke['name']}의 뼈때리는 팩트폭격! 나에게 {opp_dmg}의 엄청난 피해!")
                else:
                    st.session_state.battle_log.append(f"🔴 {opp_poke['name']}의 반격! 나에게 {opp_dmg}의 피해를 입혔다.")
                st.session_state.my_hp -= opp_dmg
            
            # 3. 누군가 쓰러졌는지 확인 기록
            if st.session_state.opp_hp <= 0:
                st.session_state.battle_log.append(f"🏆 {opp_poke['name']}이(가) 쓰러졌다! 당신의 승리입니다!")
                st.balloons()
            elif st.session_state.my_hp <= 0:
                st.session_state.battle_log.append(f"💀 {my_poke['name']}이(가) 쓰러졌다... 눈앞이 깜깜해졌다.")
            
            st.rerun() # 체력과 로그를 갱신하기 위해 화면 새로고침

    # 누군가 HP가 0이 되어 배틀이 끝난 경우
    else:
        st.error("배틀 종료!")
        if st.button("🔄 새로운 배틀 시작하기", use_container_width=True):
            # 게임 상태를 초기화하고 처음 선택 화면으로 돌아갑니다.
            st.session_state.game_mode = 'select'
            st.rerun()
