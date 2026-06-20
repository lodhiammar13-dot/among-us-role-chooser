import streamlit as st
import random

st.set_page_config(page_title="Among Us IRL", page_icon="🚀")

ROLES = [
    "😈 Impostor",
    "🤡 Jester",
    "🔧 Engineer",
    "⭐ Sheriff",
    "📢 Noise Maker"
]

# ---------------- Session State ----------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "players" not in st.session_state:
    st.session_state.players = []

if "roles" not in st.session_state:
    st.session_state.roles = []

if "current" not in st.session_state:
    st.session_state.current = 0

if "revealed" not in st.session_state:
    st.session_state.revealed = False


st.title("🚀 Among Us IRL Role Generator")

# ================== SETUP ==================
if not st.session_state.game_started:

    names = []

    for i in range(5):
        names.append(st.text_input(f"Player {i+1}", key=f"name{i}"))

    if st.button("🎲 Generate Roles"):

        if any(name.strip() == "" for name in names):
            st.error("Please enter all player names.")

        elif len(set(names)) != 5:
            st.error("Player names must be unique.")

        else:
            shuffled = ROLES.copy()
            random.shuffle(shuffled)

            st.session_state.players = names
            st.session_state.roles = shuffled
            st.session_state.current = 0
            st.session_state.revealed = False
            st.session_state.game_started = True

            st.rerun()

# ================== GAME ==================
else:

    i = st.session_state.current

    if i >= len(st.session_state.players):

        st.success("🎉 Everyone has received their role!")

        if st.button("🔄 New Game"):

            # Clear everything from session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]

            st.rerun()

    else:

        player = st.session_state.players[i]
        role = st.session_state.roles[i]

        st.header(f"📱 Pass the device to **{player}**")

        if not st.session_state.revealed:

            st.write("👀 Make sure nobody else is looking at the screen!")

            if st.button("Reveal My Role"):
                st.session_state.revealed = True
                st.rerun()

        else:

            st.markdown("---")
            st.markdown(f"# {role}")
            st.markdown("---")

            if st.button("➡️ Next Player"):
                st.session_state.revealed = False
                st.session_state.current += 1
                st.rerun()
                st.rerun()
