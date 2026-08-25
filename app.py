import streamlit as st

st.set_page_config(page_title="লোকাস AI", page_icon="🤖")

st.title("🤖 লোকাস AI")
st.write("আমি লোকাস, তোমার ব্যক্তিগত AI অ্যাসিস্ট্যান্ট।")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "হ্যালো! আমি লোকাস। কিভাবে সাহায্য করতে পারি?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("এখানে টাইপ করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    reply = f"তুমি বলেছ: '{prompt}'\n\nআমি লোকাস, এখনো শিখছি!"
    if "নাম" in prompt:
        reply = "আমার নাম লোকাস! তোমার নাম কি?"
    elif "কেমন আছ" in prompt:
        reply = "আমি ভালো আছি, তুমি কেমন আছ?"
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
