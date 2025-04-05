---

# 😊 **Emotion Detection Web App**  

## 🚀 **Live Demo**  
🔗 [Click here to view the app](https://emotiondetectionapp-ubu0.onrender.com)  

---

## 📌 **About the Project**  
This is an **AI-powered Emotion Detection Web App** that predicts the **emotion expressed in text** using a trained **Machine Learning model**.

🔍 **Built with:**  
- **Backend:** Flask  
- **Frontend:** HTML/CSS  
- **ML Model:** Scikit-learn  
- **Deployment:** Render  
The app accepts text input and returns the predicted emotion. It supports both **form submissions** and **REST API calls**.

---

## 🎯 **Features**  
- ✅ Detects emotions from text input  
- ✅ Predicts emotions like **Joy**, **Sadness**, **Anger**, **Love**, **Fear**, **Surprise**  
- ✅ Clean and responsive UI with background styling  
- ✅ REST API with JSON input/output  
- ✅ Testable via **Postman** or **cURL**  
- ✅ **Deployed on Render** for easy access  

---

## 🛠️ **Tech Stack**  
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

## 📂 **Folder Structure**  

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

## 💻 **How to Run Locally**  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/AnaghaSathyanarayanan/EmotionDetectionApp.git
cd EmotionDetectionApp
```

### 2️⃣ **Set Up a Virtual Environment**  
```bash
python -m venv env
# Activate the environment
env\Scripts\activate      # On Windows
source env/bin/activate   # On Mac/Linux
```

### 3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Flask App**  
```bash
python app.py
```

**Visit** 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📬 **Testing the API with Postman**  

You can test the **API endpoint** (`/predict`) using Postman or any HTTP client.

### 📥 **Step-by-step:**

1. Open Postman  
2. Set method to `POST`  
3. Enter the URL:  
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

### ✅ **Example Response:**
```json
{
  "original_text": "I am feeling fantastic today!",
  "predicted_emotion": "joy"
}
```

---

## 🌐 **Deployment on Render**  

### Step 1: **Push Your Project to GitHub**  
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### Step 2: **Deploy to Render**  
1. Go to [Render](https://render.com)  
2. Click **New Web Service**  
3. Connect your GitHub repo  
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`  
5. Click **Deploy** 🎉  

---

## ✨ **Contributing**  

Found a bug or have an idea for improvement? Feel free to **fork** this repo and submit a **pull request**. Contributions are always welcome!

---

## **Author**  
Made by [Anagha Sathyanarayanan](https://github.com/AnaghaSathyanarayanan)

---

## 🚀 **Support**  

If you need help, feel free to open an issue on GitHub or reach out to me directly! ✉️

---

### 📚 **Additional Notes**  
- You can test the API endpoint using **Postman** as described above.  
- The app supports **both** form submissions and **REST API** calls, making it flexible for integration.

---

Let me know if you'd like to add badges, Docker support, or other advanced features in the future!