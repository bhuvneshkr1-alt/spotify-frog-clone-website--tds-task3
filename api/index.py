import os
from flask import Flask, render_template

# Point paths to project root (one directory above /api)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')

app = Flask(
    __name__, 
    template_folder=template_dir, 
    static_folder=static_dir
)

tracks = [
    {
        "id": 1,
        "title": "7 years",
        "artist": "lukas Graham",
        "file": "audio/song2.mp3",
        "cover": "https://wikimedia.org"
    },
    {
        "id": 2,
        "title": "taare",
        "artist": "Synthwave Retro",
        "file": "audio/song1.mp3",
        "cover": "https://genius.com"
    }
]

@app.route('/')
def index():
    return render_template('index.html', tracks=tracks)

@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html', tracks=tracks)

if __name__ == '__main__':
    app.run(debug=True)
