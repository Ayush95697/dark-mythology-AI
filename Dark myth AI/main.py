import streamlit as st
from backend import create_llm, get_answer, get_database_info, update_llm_settings

# Page setup
st.set_page_config(
    page_title="Dark Mythology Explorer",
    page_icon="🧙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize backend after Streamlit page configuration
create_llm()

# Custom CSS for dark demonic theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Nosifer&family=Butcherman&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0000 30%, #330000 70%, #1a0000 100%);
        background-attachment: fixed;
    }

    .main-header {
        text-align: center;
        color: #ff0000;
        margin-bottom: 1rem;
        font-family: 'Nosifer', cursive;
        text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000, 0 0 60px #ff0000;
        animation: flicker 2s infinite alternate;
    }

    @keyframes flicker {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }

    .subtitle {
        text-align: center;
        color: #cc0000;
        font-style: italic;
        margin-bottom: 2rem;
        font-family: 'Butcherman', cursive;
        text-shadow: 0 0 10px #cc0000;
        font-size: 1.2rem;
    }

    .sidebar-section {
        margin-bottom: 1.5rem;
        padding: 1rem;
        border-radius: 10px;
        background: linear-gradient(135deg, rgba(51, 0, 0, 0.3), rgba(102, 0, 0, 0.2));
        border: 1px solid #660000;
        box-shadow: inset 0 0 10px rgba(255, 0, 0, 0.3), 0 0 20px rgba(51, 0, 0, 0.5);
        color: #ffcccc;
    }

    .source-item {
        background: linear-gradient(90deg, rgba(51, 0, 0, 0.4), rgba(102, 0, 0, 0.2));
        padding: 0.8rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #ff0000;
        border-right: 1px solid #660000;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.2);
        color: #ffdddd;
        transition: all 0.3s ease;
    }

    .source-item:hover {
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.4);
        transform: translateX(5px);
    }

    .stSidebar {
        background: linear-gradient(180deg, #1a0000 0%, #000000 50%, #1a0000 100%);
    }

    .stSidebar > div:first-child {
        background: linear-gradient(180deg, #1a0000 0%, #000000 50%, #1a0000 100%);
        border-right: 2px solid #660000;
    }

    div[data-testid="stMarkdownContainer"] h3 {
        color: #ff3333 !important;
        font-family: 'Butcherman', cursive;
        text-shadow: 0 0 10px #ff0000;
    }

    .stTextInput input {
        background-color: rgba(51, 0, 0, 0.6) !important;
        border: 2px solid #660000 !important;
        color: #ffcccc !important;
        border-radius: 10px !important;
    }

    .stTextInput input:focus {
        border-color: #ff0000 !important;
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.5) !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #660000, #330000) !important;
        color: #ffcccc !important;
        border: 2px solid #ff0000 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #990000, #660000) !important;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.5) !important;
        transform: translateY(-2px) !important;
    }

    .stExpander {
        background: rgba(51, 0, 0, 0.3) !important;
        border: 1px solid #660000 !important;
        border-radius: 10px !important;
    }

    .footer-evil {
    text-align: center;
    color: black;
    font-size: 0.9rem;
    text-shadow: 0 0 2px #ff0000; /* Reduced the shadow for better clarity */
    font-family: 'Creepster', cursive; /* A more readable horror-themed font */
    }

    /* Chat message styling */
    div[data-testid="chatMessage"] {
        background: rgba(51, 0, 0, 0.2) !important;
        border: 1px solid rgba(102, 0, 0, 0.3) !important;
        border-radius: 15px !important;
    }

    /* Slider styling */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #660000, #ff0000) !important;
    }

    /* Spinner styling */
    .stSpinner > div {
        border-top-color: #ff0000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 😈 About Dark Realm Explorer")
    st.markdown("""
    <div class="sidebar-section">
    Enter the abyss of forbidden knowledge... Summon ancient demons, explore cursed legends, and uncover the darkest secrets that mortals fear to whisper. 
    The shadows hold answers for those brave enough to seek them.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔥 Infernal Settings")
    with st.expander("⚙️ Dark Configuration", expanded=False):
        chunk_size = st.slider(
            "👹 Soul Fragment Size",
            min_value=100,
            max_value=1000,
            value=500,
            step=50,
            help="Size of cursed text fragments"
        )

        k_retriever = st.slider(
            "🔮 Summoning Power (k)",
            min_value=1,
            max_value=10,
            value=5,
            help="Number of dark spirits to conjure"
        )

        temperature = st.slider(
            "🌋 Demonic Chaos Level",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Unleash chaotic evil in responses"
        )

    st.markdown("### 📚 Forbidden Grimoire")

    # Get real database info
    db_info = get_database_info()

    st.markdown(f"""
    <div class="sidebar-section">
    <strong>🔗 Hellish Connection:</strong> {db_info['status']}<br>
    <strong>👹 Cursed Souls:</strong> {db_info['document_count']}<br>
    <strong>🧙‍♀️ Dark Oracle:</strong> {db_info['embedding_model']}<br><br>
    <strong>🔥 Infernal Contents:</strong><br>
    • Demonic mythologies<br>
    • Cursed folklore<br>
    • Forbidden grimoires<br>
    • Supernatural horrors<br>
    • Dark rituals & magic<br>
    </div>
    """, unsafe_allow_html=True)

    # Clear chat button
    if st.button("🗑️ Banish All Spirits", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main content
st.markdown('<h1 class="main-header">👹 DARK REALM EXPLORER 👹</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">🔥 Summoning forbidden knowledge from the depths of hell 🔥</p>', unsafe_allow_html=True)

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
chat_container = st.container()

# Display chat history
with chat_container:
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            with st.chat_message("user", avatar="😈"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant", avatar="👹"):
                # Split content and sources if they exist
                content = msg["content"]
                if "📖 **Sources:**" in content:
                    main_content, sources_section = content.split("📖 **Sources:**", 1)
                    st.markdown(main_content.strip())

                    # Display sources in expander
                    with st.expander("📜 Dark Sources", expanded=False):
                        sources_list = sources_section.strip().split("\n")
                        for source in sources_list:
                            if source.strip() and source.startswith("- "):
                                st.markdown(f'<div class="source-item">{source[2:]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(content)

# User input
if prompt := st.chat_input("🔮 Whisper your dark desires to the demon..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message immediately
    with st.chat_message("user", avatar="😈"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant", avatar="👹"):
        with st.spinner("🔥 Conjuring demons from the abyss..."):
            answer, sources = get_answer(prompt, k=k_retriever, temperature=temperature)  # Use dynamic settings

            # Format response
            response = answer
            if sources:
                response += "\n\n📖 **Sources:**\n" + "\n".join([f"- {src}" for src in sources])

            # Display main answer
            if "📖 **Sources:**" in response:
                main_content, sources_section = response.split("📖 **Sources:**", 1)
                st.markdown(main_content.strip())

                # Display sources in expander
                with st.expander("📜 Dark Sources", expanded=False):
                    sources_list = sources_section.strip().split("\n")
                    for source in sources_list:
                        if source.strip() and source.startswith("- "):
                            st.markdown(f'<div class="source-item">{source[2:]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(response)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.markdown(
    '<p class="footer-evil">🔥 Powered by Infernal AI • Enter at your own peril • May your soul find no peace 🔥</p>',
    unsafe_allow_html=True
)
