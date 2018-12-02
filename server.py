from flask import Flask, render_template
from defs import get_random_video_ru, get_random_video, most_popular_video_a_year_ago
app = Flask(__name__)

@app.route("/")
def hello():
    link = str(get_random_video())
    return render_template('youtube.html', link=link)

if __name__ == "__main__":
    app.run()
