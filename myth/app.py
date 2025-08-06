import streamlit as st
from src.myth_checker import check_myth_with_wiki

st.set_page_config(page_title="🧠 Myth Buster Chatbot", layout="centered")

st.title("🧠 Myth Buster Chatbot")
st.markdown("Ask me a common belief or myth and I'll verify it using Wikipedia and AI reasoning.")

user_input = st.text_input("📝 Enter a myth or belief you want to check:")

if user_input:
    try:
        with st.spinner("🔎 Verifying using Wikipedia..."):
            result = check_myth_with_wiki(user_input)
            st.success("✅ Here's what I found:")

            # Split result into verdict + explanation
            lines = result.split("\n")
            for line in lines:
                if line.lower().startswith("verdict:"):
                    st.markdown(f"🧾 **{line.strip()}**")
                elif line.lower().startswith("explanation:"):
                    st.markdown(f"🧠 {line.strip()}")
                else:
                    st.write(line)
    except Exception as e:
        st.error("❌ Something went wrong.")
        st.exception(e)
