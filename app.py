import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Ego-Driven Code Refactorer", page_icon="🤖", layout="centered")

# Custom CSS for styling avatar and chat bubble
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .avatar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
    .avatar-circle {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        background: linear-gradient(135deg, #4f46e5, #3b82f6);
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 40px;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }
    .chat-bubble {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #3b82f6;
        font-size: 16px;
        margin-top: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# App UI Header
st.title("🤖 Ego-Driven Code Refactorer")
st.write("Welcome to the ultimate sarcastic AI code companion for IBM Bob 2.0!")

# Code Input Section
code_input = st.text_area("Paste your Python code here:", value="""class OverEngineeredGreeter:
    def __init__(self, name):
        self.name = name
    async def generate_greeting(self):
        return lambda: f"Hello, {self.name}!"
""")

if st.button("Analyze & Roast Code 🚀"):
    # Analysis Logic
    line_count = len(code_input.strip().split('\n'))
    complexity_keywords = ['lambda', 'class', 'def', 'import', 'async', 'await']
    keyword_count = sum(code_input.count(kw) for kw in complexity_keywords)
    ego_score = min(100, (line_count * 2) + (keyword_count * 10))
    
    st.subheader(f"📊 Analysis Results (Ego Score: {ego_score}%)")
    
    # Circular Avatar & Chat Simulation UI
    st.markdown("### 💬 Bob's Companion Chat Room")
    
    st.markdown("""
        <div class="avatar-container">
            <div class="avatar-circle">🤖</div>
        </div>
    """, unsafe_allow_html=True)
    
    if ego_score > 70:
        message = "Hey artist! You wrote code like you're building a spacecraft for NASA! Let's simplify it before it crashes."
    elif ego_score > 40:
        message = "Hey there! I am here if you need to tone down the over-engineering a bit."
    else:
        message = "Clean and humble code! I am here anytime you need."
        
    st.markdown(f"""
        <div class="chat-bubble">
            <strong>Bob:</strong> {message}
        </div>
    """, unsafe_allow_html=True)