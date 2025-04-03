import streamlit as st
import joblib

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
st.title("Emotion Detection App")
user_input = st.text_input("Enter a sentence to detect its emotion:")

if st.button("Analyze Emotion"):
    if user_input:
        # ✅ Vectorize Input
        input_features = vectorizer.transform([user_input])

        # ✅ Predict and Map the Label
        prediction = model.predict(input_features)[0]
        predicted_emotion = label_mapping.get(prediction, "Unknown")

        st.success(f"Predicted Emotion: {predicted_emotion}")
