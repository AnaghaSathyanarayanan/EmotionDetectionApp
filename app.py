import streamlit as st
import joblib

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.freepik.com/free-psd/3d-background-with-emojis_35308564.htm#fromView=keyword&page=1&position=42&uuid=8e7d454d-7550-45bd-8a51-1b59e4a46242&query=Emoji+Wallpaper");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ✅ Load model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ✅ Updated Label Mapping to Match Dataset
label_mapping = {
    0: "Sadness",
    1: "Joy",
    2: "Love",
    3: "Anger",
    4: "Fear",
    5: "Surprise"  # Match title-case format
}

# ✅ Streamlit App
st.title("😊 Emotion Detection App")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("emotion_icon.png", width=150)  # Add a small icon

with col2:
    st.subheader("Enter your text below to detect emotions")

user_input = st.text_area("Type your sentence here...")

if st.button("🚀 Detect Emotion"):
    with st.spinner("Analyzing... Please wait!"):
        result = predict_emotion(user_input)  # Call your ML function
    emotion_colors = {
        "Happy": "🟢",
        "Sad": "🔵",
        "Angry": "🔴",
        "Neutral": "⚪"
    }
    st.markdown(f"**Detected Emotion:** {emotion_colors[result]} {result}", unsafe_allow_html=True)

