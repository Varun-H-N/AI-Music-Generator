from flask import Flask, render_template, request
from generate_music import generate_music

app = Flask(__name__)

genre_images = {

"sad":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",

"happy":"https://images.unsplash.com/photo-1500534623283-312aade485b7",

"romance":"https://images.unsplash.com/photo-1516589091380-5d8e87df6999",

"action":"https://images.unsplash.com/photo-1506744038136-46273834b3fb",

"thriller":"https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d",

"edm":"https://images.unsplash.com/photo-1501386761578-eac5c94b800a",

"rock":"https://images.unsplash.com/photo-1511379938547-c1f69419868d",

"jazz":"https://images.unsplash.com/photo-1507838153414-b4b713384a76",

"lofi":"https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

"ambient":"https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",

"hiphop":"https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4",

"cinematic":"https://images.unsplash.com/photo-1489599849927-2ee91cede3ba",

"piano":"https://images.unsplash.com/photo-1513883049090-d0b7439799bf",

"horror":"https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d",

"scifi":"https://images.unsplash.com/photo-1446776811953-b23d57bd21aa"

}


@app.route("/")
def home():
    return render_template("index.html", songs=None, bg_image="")


@app.route("/generate", methods=["POST"])
def generate():

    genre = request.form["genre"]

    songs = generate_music(genre)

    bg_image = genre_images.get(genre)

    return render_template(
        "index.html",
        songs=songs,
        genre=genre,
        bg_image=bg_image
    )


if __name__ == "__main__":
    app.run(debug=True)