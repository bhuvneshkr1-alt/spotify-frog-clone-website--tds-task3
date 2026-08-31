import os
from flask import Flask, render_template

# Dynamically locate the 'templates' directory relative to this file
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

tracks = [
    {
        "id": 1,
        "title": "7 years",
        "artist": "lukas Graham",
        "file": "audio/song2.mp3",
        "cover": "https://upload.wikimedia.org/wikipedia/en/b/bc/7-Years-by-Lukas-Graham.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail_unscaled&_=20151119064620"
    },
    {
        "id": 2,
        "title": "taare",
        "artist": "Synthwave Retro",
        "file": "audio/song1.mp3",
        "cover": "https://t2.genius.com/unsafe/387x387/https%3A%2F%2Fimages.genius.com%2F565dfc3d5cd8f252a3cb8d07806632a6.640x640x1.jpg"
    }
]

@app.route('/')
def index():
    return render_template('index.html', tracks=tracks)

# Expose WSGI handler for Vercel
app = app

if __name__ == '__main__':
    app.run(debug=True)
