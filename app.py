from flask import Flask, render_template, request, jsonify
import pickle
import nltk

# Initialize Flask app
app = Flask(__name__)

# Download NLTK tokenizer if needed
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Load model and vectorizer
try:
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    with open('emotion_model.pkl', 'rb') as f:
        model = pickle.load(f)

    emotion_labels = list(model.classes_)  # Use model's class labels

    print("Model and vectorizer loaded successfully!")
except Exception as e:
    print(f"Error loading model or vectorizer: {e}")
    emotion_labels = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Handle form or JSON input
            if request.content_type == 'application/json':
                data = request.get_json()
                text = str(data.get('text', ''))
            else:
                text = str(request.form.get('text', ''))

            if not text.strip():
                return jsonify({'error': 'No text provided'})

            # Directly vectorize without cleaning
            text_vectorized = vectorizer.transform([text])
            probabilities = model.predict_proba(text_vectorized)[0]
            max_prob_index = probabilities.argmax()
            predicted_emotion = emotion_labels[max_prob_index]

            result = {
                'original_text': text,
                'predicted_emotion': predicted_emotion
            }

            if request.content_type == 'application/json':
                return jsonify(result)
            else:
                return render_template('result.html', result=result)

        except Exception as e:
            error_msg = f"Error during prediction: {str(e)}"
            print(error_msg)
            if request.content_type == 'application/json':
                return jsonify({'error': error_msg})
            else:
                return render_template('error.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)
