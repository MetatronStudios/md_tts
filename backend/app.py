from flask import Flask, jsonify, request
from flask_cors import CORS

from piper_wrapper import PiperWrapper

app = Flask(__name__)
CORS(app)
tts = PiperWrapper()


@app.route("/")
def index():
    return {"message": "Markdown TTS Reader backend"}


@app.route("/api/tts", methods=["POST"])
def tts_endpoint():
    data = request.get_json(force=True)
    text = data.get("text") if isinstance(data, dict) else None
    if not text or not isinstance(text, str):
        return jsonify({"error": "Invalid text"}), 400
    try:
        result = tts.synthesize(text)
    except Exception as exc:  # pylint: disable=broad-except
        return jsonify({"error": str(exc)}), 500
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
