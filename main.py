import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download_audio():
    data = request.json
    video_url = data.get('url')

    if not video_url:
        return jsonify({"error": "Missing 'url' in request body"}), 400

    try:
        subprocess.run([
            'yt-dlp',
            '-f', 'bestaudio',
            '--extract-audio',
            '--audio-format', 'mp3',
            video_url
        ], check=True)
        return jsonify({"status": "Download completed"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500


# 👇 Make sure this uses Railway's PORT environment variable
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
