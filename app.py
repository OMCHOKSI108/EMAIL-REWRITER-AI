import streamlit as st
import difflib
import os
import sys
from dotenv import load_dotenv
from email_rewriter import EmailRewriter, EmailConfig
from api_model_checker import APIModelChecker

# Debug: Ensure the correct module path and print debug info
print(f"Using api_model_checker from: {sys.modules['api_model_checker'].__file__}")

# Load environment variables
load_dotenv()

# --- Streamlit Page Config ---
st.set_page_config(page_title="AI Email Rewriter", page_icon="✉️", layout="wide")

# --- Custom CSS Styling ---
st.markdown("""
<style>
    .stTextArea textarea {
        font-size: 16px !important;
    }
    .diff-add { background-color: #e6ffe6; color: #006400; }
    .diff-remove { background-color: #ffe6e6; color: #640000; text-decoration: line-through; }
    .main-header { text-align: center; padding: 2rem 0; }
    .feature-box { border: 1px solid #e0e0e0; border-radius: 10px; padding: 20px; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- Diff Generator ---
def generate_diff(original: str, rewritten: str) -> str:
    diff = difflib.ndiff(original.splitlines(), rewritten.splitlines())
    html_diff = []
    for line in diff:
        if line.startswith('+ '):
            html_diff.append(f'<div class="diff-add">{line[2:]}</div>')
        elif line.startswith('- '):
            html_diff.append(f'<div class="diff-remove">{line[2:]}</div>')
        elif line.startswith('  '):
            html_diff.append(f'<div>{line[2:]}</div>')
    return ''.join(html_diff)

# --- UI Header ---
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("✨ AI Email Rewriter")
st.markdown("Transform your emails with AI-powered tone and clarity enhancement")
st.markdown("</div>", unsafe_allow_html=True)

# --- Sidebar Config ---
with st.sidebar:
    st.header("⚙️ API Settings")

    # Input for Cohere API key only
    input_cohere_key = st.text_input("🔑 Cohere API Key", type="password")
    cohere_key = input_cohere_key or os.getenv("COHERE_KEY")
    print(f"[DEBUG] Cohere API Key: {'Set' if cohere_key else 'Not set'}")

    # Debug: Inspect APIModelChecker class
    print(f"[DEBUG] APIModelChecker __init__ signature: {APIModelChecker.__init__.__code__.co_varnames}")
    checker = APIModelChecker(cohere_key=cohere_key)
    cohere_models = checker.check_cohere_models() or []

    # Model dropdown with Cohere models only
    final_model_selection = st.selectbox(
        "🧠 Select Model to Use",
        [f"Cohere: {m}" for m in cohere_models] or ["No models available"],
        help="Select a Cohere model to rewrite your email."
    )

    show_diff = st.checkbox("Show changes", value=False)

    st.markdown("---")
    st.markdown("### 📝 How to use")
    st.markdown("""
    1. Enter your Cohere API key (or use saved env key)  
    2. Paste your email  
    3. Choose tone  
    4. Select model  
    5. Click 'Rewrite Email'
    """)

# --- Main Email Input/Output Section ---
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("📥 Original Email")
    email_input = st.text_area(
        "Paste your email here",
        height=200,
        placeholder="Dear team,\n\nI wanted to follow up on..."
    )
    tone = st.selectbox("✍️ Select Tone", ["Professional", "Friendly", "Persuasive", "Apologetic"])
    submit = st.button("🚀 Rewrite Email")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-box">', unsafe_allow_html=True)
    st.subheader("📤 Rewritten Email")

    if submit:
        if not email_input.strip():
            st.warning("Please enter an email to rewrite.")
        elif final_model_selection == "No models available":
            st.error("No Cohere models available. Please check your API key and try again.")
        elif final_model_selection.startswith("Cohere:"):
            model_id = final_model_selection.replace("Cohere: ", "")
            if not cohere_key:
                st.error("Please provide a Cohere API key.")
            else:
                rewriter = EmailRewriter(api_key=cohere_key)
                validation_result = rewriter.validate_api_key()
                if validation_result["status"] != "success":
                    st.error(f"Invalid Cohere API key. {validation_result['error']}")
                else:
                    config = EmailConfig(
                        tone=tone,
                        model=model_id,
                        temperature=0.7,
                        max_tokens=1000
                    )
                    with st.spinner(f"Rewriting using {model_id}..."):
                        result = rewriter.rewrite_email(email_input, config, max_retries=3)
                        if result["status"] == "success":
                            rewritten = result["rewritten_email"]
                            if show_diff:
                                st.markdown("### Changes:")
                                diff_html = generate_diff(email_input, rewritten)
                                st.markdown(diff_html, unsafe_allow_html=True)
                            else:
                                st.text_area("Rewritten Email", rewritten, height=200)
                        else:
                            st.error(f"Cohere Error: {result['error']}")
        else:
            st.warning("Please select a valid model.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    Made with ❤️ using Streamlit and Cohere<br>
    <small>Env fallback enabled — customize `.env` for security</small>
</div>
""", unsafe_allow_html=True)