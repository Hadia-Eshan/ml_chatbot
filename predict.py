# predict.py
import joblib
from utils import preprocess, responses

# Load model and vectorizer
model = joblib.load("chatbot_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Chat loop
print("🤖 RestaurantBot: Hi! Ask me anything or type 'exit' to quit.")
while True:
    user_input = input("👤 You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("🤖 RestaurantBot: Goodbye!")
        break

    processed = preprocess(user_input)
    intent = model.predict(vectorizer.transform([processed]))[0]
    response = responses.get(intent, f"(Intent: {intent}) Sorry, I didn't understand.")
    print(f"🤖 RestaurantBot: {response}")
