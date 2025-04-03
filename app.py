import streamlit as st
import joblib
import base64

# ✅ Function to set background image
def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    img_base64 = base64.b64encode(img_data).decode()  # ✅ Corrected Encoding

    # ✅ Inject CSS for background image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{img_base64}");
            background-size: cover;
            background-position: center;
        }}
        h3 {{
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px black;
            font-size: 28px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Set the background
set_background("assets/emotion_icon.jpg")  # Adjust path if needed

# ✅ Load trained model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ✅ Emotion label mapping with emojis ✨
label_mapping = {
    0: "😢 **Sadness**",
    1: "😊 **Joy**",
    2: "❤️ **Love**",
    3: "😠 **Anger**",
    4: "😨 **Fear**",
    5: "😲 **Surprise**"
}

# ✅ Streamlit UI
st.title("😊 Emotion Detection App")
st.write("Enter a sentence to detect its emotion.")

# ✅ User Input
user_input = st.text_area("Enter your sentence:")

if st.button("🚀 Predict Emotion"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a valid sentence!")
    else:
        # ✅ Convert user input to model features
        input_features = vectorizer.transform([user_input])

        # ✅ Predict emotion
        prediction = model.predict(input_features)[0]  # Extract single value

        # ✅ Map numeric prediction to emotion label with emoji
        predicted_emotion = label_mapping.get(prediction, "🤔 **Unknown Emotion**")

        # ✅ Display result with black outlined text
        st.markdown(f"<h3>Predicted Emotion: {predicted_emotion}</h3>", unsafe_allow_html=True)
