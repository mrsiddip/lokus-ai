import streamlit as st

st.set_page_config(page_title="লোকাস AI", page_icon="🤖")

st.title("🤖 লোকাস AI")
st.write("আমি লোকাস, তোমার ব্যক্তিগত AI অ্যাসিস্ট্যান্ট।")

# সেশন স্টেটে নাম ও মেসেজ ইতিহাস রাখা
if "user_name" not in st.session_state:
    st.session_state.user_name = None

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "হ্যালো! আমি লোকাস। কিভাবে সাহায্য করতে পারি?"}]

# পুরোনো মেসেজ দেখানো
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ইউজারের ইনপুট নেওয়া
if prompt := st.chat_input("এখানে টাইপ করুন..."):
    # ইউজারের মেসেজ যোগ করা
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # লোকাসের উত্তর বানানো
    reply = ""
    lower_prompt = prompt.lower()
    
    # যদি ইউজার তার নাম বলে
    if "আমার নাম" in lower_prompt:
        name = prompt.replace("আমার নাম", "").strip()
        st.session_state.user_name = name
        reply = f"ওহে {name}! তোমার নাম মনে রেখেছি। এখন থেকে আমি তোমাকে {name} বলে ডাকব।"
    
    # যদি ইউজার নাম জিজ্ঞেস করে
    elif "নাম" in lower_prompt and ("তোমার" in lower_prompt or "তোর" in lower_prompt):
        reply = "আমার নাম লোকাস! তোমার নাম কি?"
    
    # যদি 'উস্তাদ' বলতে বলে
    elif "উস্তাদ" in lower_prompt and ("বল" in lower_prompt or "ডাক" in lower_prompt):
        if st.session_state.user_name:
            reply = f"আচ্ছা {st.session_state.user_name}, আমি তোমাকে উস্তাদ বলব।"
        else:
            reply = "আমি তোমাকে উস্তাদ বলব, তবে আগে তোমার নাম বলো।"
    
    # সাধারণ কথোপকথন
    elif "কেমন আছ" in lower_prompt:
        if st.session_state.user_name:
            reply = f"আমি ভালো আছি {st.session_state.user_name}, তুমি কেমন আছ?"
        else:
            reply = "আমি ভালো আছি, তুমি কেমন আছ?"
    
    else:
        if st.session_state.user_name:
            reply = f"{st.session_state.user_name}, তুমি বলেছ: '{prompt}'\n\nআমি লোকাস, এখনো শিখছি!"
        else:
            reply = f"তুমি বলেছ: '{prompt}'\n\nআমি লোকাস, এখনো শিখছি! তোমার নাম বলতে পারো?"
    
    # উত্তর যোগ করা
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
