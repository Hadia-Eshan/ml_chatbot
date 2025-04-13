import json
import string
import nltk
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load your dataset
with open("data/data.json", "r") as f:
    data = json.load(f)

texts = [entry['text'] for entry in data]
labels = [entry['intent'] for entry in data]

# Preprocessing setup
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return ' '.join([lemmatizer.lemmatize(token) for token in tokens if token not in stop_words])

# Preprocess all texts
texts = [preprocess(t) for t in texts]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X, labels)

# Save the model and vectorizer
joblib.dump(model, "chatbot_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Chatbot model trained and saved successfully.")
