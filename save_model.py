import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Step 1: Load the dataset
data = pd.read_csv("Emotion.csv")  # Make sure this file is in the same folder as this script

# Step 2: Convert text to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Sentence"])  # 'Sentence' column has text
y = data["Sentiment"]  # 'Sentiment' column has labels (Positive, Negative, Neutral)

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 5: Save the trained model and vectorizer
joblib.dump(model, "emotion_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and vectorizer saved successfully!")
