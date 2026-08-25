import streamlit as st

st.set_page_config(page_title="লোকাস AI", page_icon="🤖")

# ----- সাইডবারে লোগো ও প্রোফাইল পিকচার -----
with st.sidebar:
    st.image("logo.png", width=150)  # আপনার লোগো
    st.divider()
    st.image("my_photo.jpg", width=200, caption="🧑‍💻 আমার মালিক")
    st.caption("লোকাস AI - সংস্করণ ১.০")

# ----- মূল চ্যাট ইন্টারফেস -----
st.title("🤖 লোকাস AI")
st.write("আমি লোকাস, তোমার ব্যক্তিগত AI অ্যাসিস্ট্যান্ট।")

# সেশন স্টেট
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "হ্যালো! আমি লোকাস। কিভাবে সাহায্য করতে পারি?"}]

# মেসেজ দেখানো
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ইউজারের ইনপুট
if prompt := st.chat_input("এখানে টাইপ করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    reply = ""
    lower_prompt = prompt.lower()
    
    # নাম মনে রাখা
    if "আমার নাম" in lower_prompt:
        name = prompt.replace("আমার নাম", "").strip()
        st.session_state.user_name = name
        reply = f"ওহে {name}! তোমার নাম মনে রেখেছি।"
    elif "নাম" in lower_prompt and ("তোমার" in lower_prompt or "তোর" in lower_prompt):
        reply = "আমার নাম লোকাস! তোমার নাম কি?"
    elif "কেমন আছ" in lower_prompt:
        if st.session_state.user_name:
            reply = f"আমি ভালো আছি {st.session_state.user_name}, তুমি কেমন আছ?"
        else:
            reply = "আমি ভালো আছি, তুমি কেমন আছ?"
    # সাধারণ উত্তর
    else:
        if st.session_state.user_name:
            reply = f"{st.session_state.user_name}, তুমি বলেছ: '{prompt}'"
        else:
            reply = f"তুমি বলেছ: '{prompt}'\n\nআমি লোকাস, এখনো শিখছি! তোমার নাম বলতে পারো?"
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
