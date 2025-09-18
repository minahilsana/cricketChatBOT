from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import logging
from llm import get_cricket_answer

app = Flask(__name__, static_folder="static")
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cricket-chatbot")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    body = request.get_json(silent=True) or {}
    question = (body.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Missing question"}), 400

    answer = get_cricket_answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    logger.info("Starting Flask app...")
    app.run(host="0.0.0.0", port=7860, debug=True)
