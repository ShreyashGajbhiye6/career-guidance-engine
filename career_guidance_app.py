import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Dummy data for demonstration
career_profiles = {
    "Doctor": "Helping people through medicine and biology",
    "Engineer": "Solving technical problems with science and math",
    "IAS Officer": "Leadership and public administration",
    "Lawyer": "Arguing cases and interpreting law"
}
career_embeddings = {k: model.encode(v) for k, v in career_profiles.items()}

st.title("🎯 AI Career Guidance Engine")

# Section 1: Aptitude Input
st.header("🧠 Aptitude Test")
math = st.slider("Math Aptitude (0-10)", 0, 10)
verbal = st.slider("Verbal Aptitude (0-10)", 0, 10)
reasoning = st.slider("Logical Reasoning (0-10)", 0, 10)

# Section 2: Goal & Interest
st.header("🎯 Your Goals and Interests")
goal_text = st.text_area("What are your career goals/interests?", "I love biology and helping people.")
goal_vec = model.encode(goal_text)

# Recommendation logic
similarities = {career: util.cos_sim(goal_vec, vec).item() for career, vec in career_embeddings.items()}
recommended = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:3]

# Display Results
st.header("🚀 Top Career Recommendations")
for career, score in recommended:
    st.subheader(f"{career} ({score:.2f} similarity)")
    st.write(career_profiles[career])

# Skill gap suggestion (mockup)
st.header("📉 Skill Gap Analysis")
if "biology" not in goal_text.lower():
    st.write("👉 Consider learning Biology to pursue a career in healthcare.")
else:
    st.write("✅ You already align well with healthcare-related careers.")
