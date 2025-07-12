# 🧠 NLP Chatbot with Flask & spaCy

A simple NLP-based chatbot built using **Python**, **Flask**, and **spaCy**. The chatbot supports intent recognition, FAQ responses, and a friendly web interface.

---

## 🚀 Features

- Basic intent recognition using spaCy similarity
- FAQ-based conversation handling
- Simple Flask backend API
- Web front-end with chat UI, avatars, and timestamps
- Easy to customize and extend

---

## Install dependencies
- pip install -r requirements.txt

---

## Run
- python app.py
Then open your browser and go to:
📍 http://127.0.0.1:5000

---

## 🧪 Test API via CURL or Postman
curl -X POST http://127.0.0.1:5000/chat \
-H "Content-Type: application/json" \
-d "{\"message\": \"What are your working hours?\"}"


