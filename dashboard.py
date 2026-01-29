import streamlit as st
import json

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Call Intelligence Dashboard",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
with open("transcript.json", "r", encoding="utf-8") as f:
    transcript = json.load(f)

with open("analysis.json", "r", encoding="utf-8") as f:
    analysis = json.load(f)

# ---------------- HEADER ----------------
st.markdown("## 📞 AI Powered Call Intelligence Dashboard")
st.caption("Speech → Text → Understanding → Insights")

st.divider()

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "🧠 Sentiment",
    analysis["sentiment"]
)

col2.metric(
    "📊 Sentiment Score",
    round(analysis["sentiment_score"], 2)
)

col3.metric(
    "🔑 Key Topics",
    len(analysis["key_topics"])
)

st.divider()

# ---------------- SUMMARY ----------------
st.subheader("📝 Call Summary")
st.info(analysis["call_summary"])

# ---------------- KEY TOPICS ----------------
st.subheader("🔑 Key Topics Discussed")

topic_cols = st.columns(len(analysis["key_topics"]))
for col, topic in zip(topic_cols, analysis["key_topics"]):
    col.success(topic)

st.divider()

# ---------------- TRANSCRIPT ----------------
st.subheader("🎧 Call Transcript (Timestamped)")

for seg in transcript["segments"]:
    st.markdown(
        f"""
        <div style="padding:8px;border-left:4px solid #4CAF50;margin-bottom:6px;">
        <b>{seg['start']}s – {seg['end']}s</b><br>
        {seg['text']}
        </div>
        """,
        unsafe_allow_html=True
    )
