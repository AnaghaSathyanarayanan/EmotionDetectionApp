---

# 😊 Emotion Detection Sentiment Analysis  

![Demo GIF](https://media.giphy.com/media/QTfX9Ejfra3ZmNxh6B/giphy.gif)  

## 🚀 Live Demo  
🔗 [Click here to view the app](https://emotiondetectionapp-hrak.onrender.com)  

## 📌 About the Project  
This project is an **AI-powered emotion detection system** that classifies text into different emotions using **Machine Learning and Natural Language Processing (NLP)**.  

### 🔍 **Features**  
✅ Detects emotions from text input in real-time  
✅ Supports multiple emotions (e.g., Happiness, Sadness, Anger, Fear, Surprise)  
✅ Simple and user-friendly **Streamlit UI**  
✅ Deployed on **Render** for easy access  

---

## 🛠️ Tech Stack  

| Technology    | Description |
|--------------|------------|
| 🐍 **Python** | Backend logic |
| 🎨 **Streamlit** | UI framework |
| 🤖 **Scikit-learn** | ML model |
| 📦 **Joblib** | Model storage |
| ☁ **Render** | Deployment |

---

## 📂 Folder Structure  

```
EmotionDetectionApp/
│── assets/                  # Images & icons
│── emotion_model.pkl        # Trained ML model
│── vectorizer.pkl           # Text feature extractor
│── app.py                   # Main Streamlit app
│── requirements.txt         # Dependencies
│── README.md                # Documentation (this file)
│── Emotion_detection.ipynb  # Jupyter Notebook for model training & evaluation
```

---

## 🚀 How to Run Locally  

### 🔹 **Step 1: Clone the Repository**  
```bash
git clone https://github.com/AnaghaSathyanarayanan/EmotionDetectionApp
cd EmotionDetectionApp
```
  
### 🔹 **Step 2: Create a Virtual Environment**  
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```
  
### 🔹 **Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```
  
### 🔹 **Step 4: Run the App**  
```bash
streamlit run app.py
```
📌 Now, open your browser and go to **`http://localhost:8501/`** 🚀  

---

## 🌎 Deployment on Render  

### 🔹 **Step 1: Push to GitHub**  
```bash
git add .
git commit -m "Deploying to Render"
git push origin main
```

### 🔹 **Step 2: Deploy on Render**  
1. Go to [Render](https://render.com/)  
2. Click **New Web Service**  
3. Connect your GitHub repository  
4. Select **Python** as the environment  
5. Set **Start Command** as:  
   ```bash
   streamlit run app.py
   ```
6. Click **Deploy** 🎉  

---

## 🎭 Preview  
📌 *Watch a quick demo of the app below!*  
![Streaming GIF](https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif)  

---  

💡 **Have ideas for improvements?** Feel free to contribute! 🚀  

---
