import streamlit as st
import time

# --- Company Info ---
company_name = "TechNova Solutions"
company_intro = f"""
Welcome to **{company_name}**!  
We specialize in delivering high-quality tech solutions, including AI development, custom software, and digital transformation consulting.
"""

# --- FAQ Dictionary ---
faq_responses = {
    "what services do you offer": "We offer AI development, custom software, web apps, and digital consulting.",
    "how can i contact you": "You can contact us at contact@technova.com or call us at +92-000-0000000.",
    "where are you located": "Our main office is located in Lahore, Pakistan.",
    "what are your working hours": "We are open Monday to Friday, 9:00 AM to 6:00 PM.",
    "do you provide support after delivery": "Yes, we provide 3 months of free support after delivery, with optional extended plans.",
    "how to get a quote": "You can fill out the contact form on our website or email your project details to contact@technova.com.",
    "introduce yourself": company_intro,
    "who are you": company_intro,
}

# --- Get Smart Response ---
def get_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # 1. Try full match
    for question, answer in faq_responses.items():
        if question in user_input:
            return answer

    # 2. Try keyword-based matching
    keywords_map = {
        "services": faq_responses["what services do you offer"],
        "contact": faq_responses["how can i contact you"],
        "location": faq_responses["where are you located"],
        "support": faq_responses["do you provide support after delivery"],
        "quote": faq_responses["how to get a quote"],
        "working hours": faq_responses["what are your working hours"],
        "introduce": faq_responses["introduce yourself"],
        "who are you": faq_responses["who are you"],
    }

    for keyword, answer in keywords_map.items():
        if keyword in user_input:
            return answer

    return "I'm sorry, I couldn't understand that. Please ask a relevant question from our FAQ."


# --- Streamlit Config ---
st.set_page_config(page_title="TechNova Chatbot", page_icon="🤖")
st.title("💬 Welcome to TechNova Chatbot")

# --- Sidebar Branding ---
with st.sidebar:
    #st.image("https://img.icons8.com/clouds/100/artificial-intelligence.png", width=80)
    st.markdown(f"### 👨‍💼 {company_name}")
    st.markdown("Empowering businesses with smart tech.\n\n[Visit Website](https://technova.fake)")
    st.markdown("---")
    st.markdown("Built with using Streamlit\n[View Code](https://github.com/yourusername/yourchatbotrepo)")

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Clear Chat Button ---
if st.button("🔁 Clear Chat"):
    st.session_state.chat_history = []

# --- Chat Input ---
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.chat_history.append(("You", user_input))
    # Get bot response
    bot_response = get_response(user_input)
    # Add bot response
    st.session_state.chat_history.append(("Bot", bot_response))

# --- Display Chat History (after input/response)
for sender, message in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        if sender == "Bot":
            with st.spinner("Typing..."):
                time.sleep(1.0)
        st.markdown(message)

# --- Download Chat History Button ---
if st.session_state.chat_history:
    chat_log = "\n".join([f"{sender}: {msg}" for sender, msg in st.session_state.chat_history])
    st.download_button("⬇ Download Chat", chat_log, file_name="chat_history.txt")
