from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch
import onnxruntime
import faiss
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load DistilBERT (Lighter than BERT)
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased-distilled-squad')
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')

# Load context from a text file
def load_context():
    with open("context.txt", "r", encoding="utf-8") as file:
        return file.read()

# Additional context for greetings
greeting_context = {
    "hello": "Hello! How can I assist you?",
    "hi": "Hi there! How’s your day going?",
    "hey": "Hey! What can I do for you?",
    "good morning": "Good morning! Hope you have a great day!",
    "good afternoon": "Good afternoon! How may I help you?",
    "good evening": "Good evening! What do you need assistance with?",
}

# Persistent user sessions for chat history
user_sessions = {}

# FAISS for fast context search
context_data = load_context()
vector_dim = 768  # Embedding size
index = faiss.IndexFlatL2(vector_dim)
vectors = np.random.rand(1000, vector_dim).astype('float32')  # Dummy embeddings
index.add(vectors)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id', 'default')  # User-specific session
    user_message = data.get('message', '').lower()  # Convert to lowercase

    # Handle greetings dynamically
    if user_message in greeting_context:
        return jsonify({'reply': greeting_context[user_message]})

    # Retrieve chat history
    history = user_sessions.get(user_id, "")

    # Combine history with current message
    new_context = f"{history}\nUser: {user_message}"

    # Tokenize input and context
    inputs = tokenizer(user_message, context_data, return_tensors='pt', truncation=True, padding=True)

    # Get model output
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract start and end logits
    start_index = torch.argmax(outputs.start_logits, dim=1).item()
    end_index = torch.argmax(outputs.end_logits, dim=1).item() + 1

    # Decode the answer
    answer_tokens = inputs['input_ids'][0][start_index:end_index]
    answer = tokenizer.decode(answer_tokens, skip_special_tokens=True)

    # Update user session
    user_sessions[user_id] = new_context

    return jsonify({'reply': answer})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
