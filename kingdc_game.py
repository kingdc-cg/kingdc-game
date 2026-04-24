import streamlit as st
import random

# --- 1. THE DATA ENGINE ---
SNACK_LIBRARY = {
    "A": {"name": "Apple Slices", "xp": 10, "power": 5, "icon": "🍎"},
    "B": {"name": "Banana Bread", "xp": 15, "power": 8, "icon": "🍞"},
    "C": {"name": "Cheetos", "xp": 5, "power": 3, "icon": "🎷"},
    "D": {"name": "Donuts", "xp": 20, "power": 10, "icon": "🍩"},
    "E": {"name": "Egg Rolls", "xp": 25, "power": 12, "icon": "🌯"},
    "F": {"name": "Fries", "xp": 12, "power": 6, "icon": "🍟"},
    "G": {"name": "Grapes", "xp": 18, "power": 7, "icon": "🍇"},
    "H": {"name": "Hot Dog", "xp": 30, "power": 15, "icon": "🌭"},
    "I": {"name": "Ice Cream", "xp": 22, "power": 9, "icon": "🍦"},
    "J": {"name": "Jelly Beans", "xp": 8, "power": 2, "icon": "🫘"},
    "K": {"name": "Kebab", "xp": 35, "power": 18, "icon": "🍢"},
    "L": {"name": "Lollipop", "xp": 5, "power": 1, "icon": "🍭"},
    "M": {"name": "Muffins", "xp": 25, "power": 11, "icon": "🧁"},
    "N": {"name": "Nachos", "xp": 15, "power": 7, "icon": "🧀"},
    "O": {"name": "Oatmeal", "xp": 12, "power": 5, "icon": "🥣"},
    "P": {"name": "Popcorn", "xp": 10, "power": 4, "icon": "🍿"},
    "Q": {"name": "Quiche", "xp": 40, "power": 20, "icon": "🥧"},
    "R": {"name": "Rice Cakes", "xp": 7, "power": 2, "icon": "🍘"},
    "S": {"name": "Snickers", "xp": 20, "power": 10, "icon": "🍫"},
    "T": {"name": "Tacos", "xp": 30, "power": 14, "icon": "🌮"},
    "U": {"name": "Ube Cake", "xp": 45, "power": 25, "icon": "🍰"},
    "V": {"name": "Vanilla", "xp": 15, "power": 6, "icon": "🍦"},
    "W": {"name": "Waffles", "xp": 25, "power": 13, "icon": "🧇"},
    "X": {"name": "Xylocarp", "xp": 50, "power": 30, "icon": "🥥"},
    "Y": {"name": "Yogurt", "xp": 20, "power": 8, "icon": "🥣"},
    "Z": {"name": "Zucchini", "xp": 10, "power": 4, "icon": "🥒"}
}

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="Kingdc Game", page_icon="👑", layout="wide")

# --- 3. STATE INIT ---
defaults = {
    'chances': 5,
    'xp': 0,
    'inventory': [],
    'atk': 15,
    'rat_hp': 100,
    'has_crown': False,
    'logs': ["System Initialized. Awaiting Commander..."]
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --- 4. HEADER ---
st.title("👑 KINGDC GAME")

# --- 5. SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/crown.png", width=80)
    name = st.text_input("Player Name:", value="Kingdc")

    st.write("XP:", st.session_state.xp)
    st.write("ATK:", st.session_state.atk)

    if st.button("Reset"):
        for key in defaults:
            st.session_state[key] = defaults[key]
        st.rerun()

# --- 6. GAME ---
tab1, tab2, tab3 = st.tabs(["Scavenge", "Shop", "Boss"])

# --- SCAVENGE ---
with tab1:
    if st.session_state.chances > 0:
        pick = st.selectbox("Pick (A-Z)", list(SNACK_LIBRARY.keys()))

        if st.button("Collect"):
            item = SNACK_LIBRARY[pick]
            st.session_state.inventory.append(item['name'])
            st.session_state.xp += item['xp']
            st.session_state.atk += item['power']
            st.session_state.chances -= 1
            st.success(f"Got {item['name']}")

    else:
        st.error("No chances left")

# --- SHOP ---
with tab2:
    if st.button("Buy Life (75 XP)"):
        if st.session_state.xp >= 75:
            st.session_state.xp -= 75
            st.session_state.chances += 1

# --- BOSS ---
with tab3:
    st.write("Rat HP:", st.session_state.rat_hp)

    if st.session_state.rat_hp > 0:
        if st.button("Attack"):
            dmg = max(1, random.randint(st.session_state.atk - 5, st.session_state.atk + 5))
            st.session_state.rat_hp -= dmg

            if st.session_state.rat_hp <= 0:
                st.success("You defeated the rat!")
                st.session_state.has_crown = True
    else:
        st.success("You are the KING 👑")