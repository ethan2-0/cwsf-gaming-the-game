from flask import Flask
from flask_cors import CORS, cross_origin

words = []
with open("words.txt", "r") as f:
    words = [x.replace("\n", "") for x in f.readlines()]

size = len(words) * 100
prime = 257

def get_word(index_in):
    index = (prime * index_in) % size
    least_significant = index % 100
    most_significant = (index - (index % 100)) // 100
    return "%s%s" % (words[most_significant], least_significant)


if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app)

    @app.route("/word/<int:index>")
    def serve_word(index):
        return get_word(index)

    app.run(port=5001)
