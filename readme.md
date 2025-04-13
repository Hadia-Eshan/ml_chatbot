# 🤖 ML Chatbot – Restaurant Assistant

This project is a machine learning–powered chatbot that simulates a restaurant manager. Users can ask questions about opening hours, menus, reservations, events, and more. The chatbot understands user input, classifies the intent using an ML model, and responds accordingly through a web interface built with Streamlit.

---

## 📦 Features

- Chatbot trained on a custom JSON dataset of restaurant-related questions
- Machine learning–based intent classification using TF-IDF and Logistic Regression
- Real-time chat UI powered by Streamlit
- Preprocessing with NLTK (tokenization, lemmatization, stopwords)
- Containerized with Docker
- Deployable to Google Cloud Run

---

## 🧱 Tech Stack

- Python 3.10
- Poetry
- NLTK
- Scikit-learn
- Streamlit
- Docker
- Google Cloud Run

---

## 🚀 Installation

Follow these steps to run the chatbot locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ml_chatbot.git
cd ml_chatbot
```
### 2. Install Poetry (if not installed)
```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
poetry --version
```

### 3.  Install dependencies
```bash 
poetry install --no-root
```

### 3.  Download NLTK resources
```bash 
poetry run python -m nltk.downloader punkt wordnet stopwords
```

## Running Project

### 1. Train Model
```bash
poetry run python train.py
```
This generates:

chatbot_model.pkl (trained model)

vectorizer.pkl (TF-IDF vectorizer)

### 2. Run With Streamlit
```bash
poetry run streamlit run app.py
```
http://localhost:8501

### 2. Run With cmd
```bash
poetry run predit.py
```
http://localhost:8501


### Use Docker
### 1. Install Docker in the system.
### 2. Build with Docker
```bash 
docker build -t chatbot-app
```
### 3. Run Locally with Docker
```bash
docker run -p 8501:8501 chatbot-app
```


## Google Cloud Run Deployment
### 1. Build and push container
```bash 
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/chatbot-app
```
### 2. Deploy service
```bash gcloud run deploy chatbot-app \
  --image gcr.io/YOUR_PROJECT_ID/chatbot-app \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 1Gi \
  --port 8501
```

## ✍️ Author
**Hadia Eshanzada**  
GitHub: [@Hadia-Eshan](https://github.com/Hadia-Eshan)
