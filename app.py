..# Import necessary modules
from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as genai

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Replace with your Gemini API key
GEMINAI_API_KEY = "AIzaSyAmKtLwOMfaNeEGz6jbMdE65epmoKNq3LE"
genai.configure(api_key=GEMINAI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Assistant's name
ASSISTANT_NAME = "Fira"

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Check if the user is asking about the assistant's name
        if any(phrase in user_message.lower() for phrase in ["your name", "who are you", "what is your name"]):
            bot_reply = f"My name is {ASSISTANT_NAME}."
        else:
            # Generate content using Geminai API
            response = model.generate_content(user_message)
            bot_reply = response.text  # Assuming the response has the 'text' attribute

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": f"Request failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
