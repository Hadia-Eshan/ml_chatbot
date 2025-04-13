# utils.py
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')
# os.environ["NLTK_DATA"] = "/usr/share/nltk_data"


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return ' '.join([lemmatizer.lemmatize(t) for t in tokens if t not in stop_words])

responses = {
    "greeting": "Hello! Welcome to our restaurant. How can I assist you today?",
    "goodbye": "Goodbye! Hope to serve you again soon.",
    "thanks": "You're welcome! Always happy to help.",
    "menu": "Sure! You can view our full menu on our website or I can list a few popular dishes.",
    "hours": "We are open from 10 AM to 10 PM, every day.",
    "location": "We're located at 123 Main Street, Downtown. Free parking available!",
    "reservation": "Absolutely! For how many people and what time?",
    "order_food": "Great! Would you like delivery or pickup?",
    "cancel_order": "I’m sorry to hear that. Let me help you cancel your order.",
    "delivery_time": "Delivery usually takes 30–45 minutes depending on your location.",
    "payment_methods": "We accept cash, credit cards, PayPal, and contactless payments.",
    "dietary_options": "Yes! We have vegan, gluten-free, and dairy-free options.",
    "contact": "You can call us at (555) 123-4567 or email contact@restaurant.com",
    "complaint": "We're really sorry to hear that. Please share more details so we can make it right.",
    "specials": "Today's specials include grilled salmon and a 2-for-1 pizza deal!",
    "group_booking": "We'd love to host your group! Let me check available tables.",
    "events": "Yes, we host private events. Would you like to book a party room?",
    "alcohol": "Yes, we serve wine, beer, and cocktails. Please bring a valid ID.",
    "kids": "Absolutely — we have a kids menu, high chairs, and a play area!"
}
