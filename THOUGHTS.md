🤔 THOUGHTS.md – Design & Learning Log
🎯 Product Thinking
Designed for Indian students aged 15–22, covering high school and early college.

Goal: Simulate a counselor-style experience using data + conversation.

Modular interface: Aptitude → Goals → Skills → Recommendations.

Adaptable for NEP pathways, regional languages, and future government APIs.

🧠 ML/NLP Design Decisions
Aptitude Prediction
Model: Random Forest Classifier (interpretable + robust)

Reason: Works well for categorical psychometric data.

Goal & Interest Extraction
Model: Sentence-BERT for embeddings

Tools: Whisper API for audio-to-text transcription

Reason: Needed deep semantic understanding of varied inputs.

Skill Matching
Approach: Sentence-BERT embeddings + cosine similarity

Challenge: Creating clean vectors for multi-disciplinary skills

Recommendation Logic
Base Logic: Rule-based links between exams (JEE → Engineering, NEET → Medicine)

Refinement: ML ranking on profile similarity

Reason: Combine explainability with personalization

Skill Gap Engine
Model: K-Nearest Neighbors for profile proximity

Courses: Curated NEP-aligned Coursera, NPTEL, and SWAYAM links

📈 Learnings
NLP understanding of user inputs required good preprocessing (especially Hindi-English mix).

Indian academic data is fragmented → building a robust ontology was hard.

Visual explainability helped gain trust in AI outputs.

Many students lack awareness of career paths → UI had to educate as well.

🚧 Challenges
Audio transcription for Indian accents

Merging structured test data with unstructured language data

Limited public datasets that link skills with Indian careers

🔮 Roadmap
Chatbot interface for dynamic career Q&A

Regional language NLP using AI4Bharat

Resume/LinkedIn scraping

Real-time dashboard with career readiness index

👤 Author
Shreyash Gajbhiye – Sole contributor: NLP pipeline, UI, ML models, documentation
