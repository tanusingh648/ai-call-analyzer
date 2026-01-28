import streamlit as st

# ⚠️ MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="AI Call Analyzer")

st.title("📞 AI Powered Call Analyzer")
st.write("✅ If you can see this, Streamlit is rendering correctly.")

st.markdown("---")

st.subheader("📡 Call Information")
st.write("Caller: Unknown Number")
st.write("Status: Call Active")

st.markdown("---")

st.subheader("⚠ Fraud Risk Level")
st.progress(85)
st.error("HIGH RISK (85%) – Possible Scam Call")

st.markdown("---")

st.subheader("📝 Live Call Transcript")
st.write("Hello sir, I am calling from your bank")
st.write("Your account will be blocked today")
st.write("Please share OTP immediately")

st.markdown("---")

st.subheader("🚨 Actions")
st.button("End Call")
st.button("Block Number")
st.button("Report Scam")
