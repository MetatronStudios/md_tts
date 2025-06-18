import base64
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_tts_endpoint():
    client = app.test_client()
    resp = client.post("/api/tts", json={"text": "hello world"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "audioContent" in data
    assert "mimeType" in data and data["mimeType"] == "audio/wav"
    assert "timings" in data
    assert isinstance(data["timings"], list)
    # audio content should be base64 string
    base64.b64decode(data["audioContent"])
