from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download_audio():
    video_url = request.json.get('url')
    subprocess.run([
        'yt-dlp',
        '-f', 'bestaudio',
        '--extract-audio',
        '--audio-format', 'mp3',
        video_url
    ])
    return {"status": "downloaded"}

app.run(port=5000)
