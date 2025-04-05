
# 😊 Emotion Detection Web App  

## 🚀 Live Demo  
🔗 [Click here to view the app](https://emotiondetectionapp-hrak.onrender.com)

---

## 📌 About the Project  
This is an **AI-powered Emotion Detection Web App** that predicts the **emotion expressed in text** using a trained **Machine Learning model**.  

Built using **Flask** for the backend and **HTML/CSS** for the frontend, this app takes text as input and returns the predicted emotion. The app is deployed on **Render** and supports both form submissions and **REST API calls**.

---

## 🎥 Preview  
![Streaming GIF](https://github.com/AnaghaSathyanarayanan/EmotionDetectionApp/blob/main/assets/demo.gif)  
📌 *Watch how the app works in real-time!*

---

## 🎯 Features  
- ✅ Detects emotions from text input  
- ✅ Predicts emotions like Joy, Sadness, Anger, Love, Fear, Surprise  
- ✅ Clean and responsive UI with background styling  
- ✅ REST API with JSON input/output  
- ✅ Testable via Postman or cURL  
- ✅ Deployed on Render  

---

## 🛠️ Tech Stack  

| Tool/Tech       | Purpose                            |
|-----------------|------------------------------------|
| 🐍 Python        | Core programming language          |
| 🌶 Flask         | Web framework (backend)            |
| 🧠 Scikit-learn  | ML model for emotion detection     |
| ✂️ NLTK          | Text preprocessing and tokenization|
| 🎨 HTML/CSS      | Frontend & Styling                 |
| 📁 Joblib        | Model persistence                  |
| ☁️ Render        | Deployment platform                |

---

## 📂 Folder Structure  

```
EmotionDetectionApp/
├── app.py                     # Flask app with routes and model logic
├── vectorizer.pkl             # TF-IDF vectorizer
├── emotion_model.pkl          # Trained ML model
├── requirements.txt           # Project dependencies
├── templates/
│   ├── index.html             # Input form page
│   └── result.html            # Result display page
├── static/
│   └── assets/
│       └── emotion_icon.jpg   # Background image
├── Emotion_detection.ipynb    # Jupyter Notebook for training and evaluation
└── README.md                  # This file
```

---

## 💻 How to Run Locally  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AnaghaSathyanarayanan/EmotionDetectionApp.git
cd EmotionDetectionApp
```

### 2️⃣ Set Up a Virtual Environment  
```bash
python -m venv env
# Activate the environment
env\Scripts\activate      # On Windows
source env/bin/activate   # On Mac/Linux
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App  
```bash
python app.py
```

Open your browser and visit 👉 `http://127.0.0.1:5000`

---

## 📬 Testing the API with Postman  

You can test the **API endpoint** (`/predict`) using Postman or any HTTP client.

### 📥 Step-by-step:  

1. Open Postman  
2. Set method to `POST`  
3. Enter URL:  
   ```
   http://127.0.0.1:5000/predict
   ```
4. Go to the **Body** tab → Select `raw` → Choose `JSON`  
5. Add this as the request body:
   ```json
   {
     "text": "I am feeling fantastic today!"
   }
   ```
6. Click **Send**

### ✅ Example Response:
```json
{
  "original_text": "I am feeling fantastic today!",
  "predicted_emotion": "joy"
}
```

---

## 🌐 Deployment on Render  

### Step 1: Push Your Project to GitHub  
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### Step 2: Deploy to Render  
1. Go to [https://render.com](https://render.com)  
2. Click **New Web Service**  
3. Connect your GitHub repo  
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`  
5. Click **Deploy** 🎉  

---

## ✨ Contributing  

Found a bug or have an idea for improvement? Feel free to fork this repo and submit a pull request. Contributions are always welcome!

---

## 🧑‍💻 Author  
Made with ❤️ by [Anagha Sathyanarayanan](https://github.com/AnaghaSathyanarayanan)

---

Let me know if you'd like to add badges, Docker support, or multiple language support in the future!
