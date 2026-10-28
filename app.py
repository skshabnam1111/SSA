import streamlit as st
from google import genai

st.set_page_config(page_title="SmartBrief", page_icon="📝")

st.title("🧠 SmartSummarize: AI-Powered Text Summarization Tool")
st.write("Paste any long text below to get an instant, structured summary.")

# Securely input or initialize API key
api_key = st.text_input("Enter your Google Gemini API Key", type="password")

text_to_summarize = st.text_area("Paste text here:", height=200)
summary_style = st.selectbox("Choose Style", ["📌 Bullet Points",
        "📄 Executive Paragraph",
        "🎯 Key Action Items",
        "🧠 Simple Explanation",
        "⚡ TL;DR (Too Long; Didn't Read)",
        "📚 Detailed Summary",
        "🔑 Key Takeaways",
        "❓ Question & Answer",
        "📖 Study Notes",
        "📝 Meeting Minutes",
        "📊 Pros and Cons",
        "⏳ Chronological Summary",
        "📋 Step-by-Step Summary",
        "💼 Professional Report",
        "🎓 Academic Summary"])

if st.button("Generate Summary"):
    if not api_key:
        st.error("Please enter a valid Gemini API key.")
    elif not text_to_summarize:
        st.error("Please enter some text to summarize.")
    else:
        try:
            # Initialize the client with the new google-genai SDK
            client = genai.Client(api_key=api_key)
            
            prompt = f"Summarize the following text in {summary_style}:\n\n{text_to_summarize}"
            
            with st.spinner("Generating summary..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt,
                )
                
            st.subheader("Summary Result")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")