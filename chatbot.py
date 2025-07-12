import spacy

# Load English model
nlp = spacy.load("en_core_web_md")

# Define intents and responses
intents = {
    "greeting": {
        "examples": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hello! How can I help you today?"
    },
    "goodbye": {
        "examples": ["bye", "goodbye", "see you", "take care"],
        "response": "Goodbye! Have a great day!"
    },
    "help": {
        "examples": ["help", "support", "assist", "how can you help"],
        "response": "I can help you with general questions. Try asking me about our services."
    },
    "hours": {
        "examples": ["opening hours", "when are you open", "working hours", "what time are you available"],
        "response": "Our working hours are from 9 AM to 5 PM, Monday to Friday."
    },
    "services": {
        "examples": [
            "what services do you offer",
            "tell me about your services",
            "what do you do",
            "what can you help me with"
        ],
        "response": "We offer web development, chatbot solutions, and automation tools."
    },

    "contact": {
        "examples": [
            "how can I contact you",
            "what is your email",
            "give me your contact information",
            "how do I reach you"
        ],
        "response": "You can email us at contact@example.com or call +92-123-4567890."
    },

    "default": {
        "response": "I'm sorry, I didn't understand that. Could you please rephrase?"
    }
}


def predict_intent(user_input):
    doc = nlp(user_input.lower())
    max_similarity = 0.0
    best_intent = "default"

    for intent, data in intents.items():
        for example in data.get("examples", []):
            example_doc = nlp(example)
            similarity = doc.similarity(example_doc)
            if similarity > max_similarity:
                max_similarity = similarity
                best_intent = intent

    if max_similarity < 0.7:
        return "default"
    return best_intent


def get_response(user_input):
    intent = predict_intent(user_input)
    return intents[intent]["response"]


# CLI Interface
if __name__ == "__main__":
    print("Chatbot is ready! Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
