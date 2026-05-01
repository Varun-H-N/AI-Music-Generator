**# AI Music Generator

A simple Flask web app that generates downloadable `.wav` music tracks based on a selected mood or genre.

## Features

- Generate 10 unique audio tracks per request
- Choose from 15 genres and moods
- Preview music directly in the browser
- Download generated `.wav` files
- Dynamic background image based on selected genre

## Supported Genres

`sad`, `happy`, `romance`, `action`, `thriller`, `edm`, `rock`, `jazz`, `lofi`, `ambient`, `hiphop`, `cinematic`, `piano`, `horror`, `scifi`

## Tech Stack

- Python
- Flask
- NumPy
- SciPy
- HTML/CSS/JavaScript

## Project Structure

```text
AI-Music-Generator/
├── app.py
├── generate_music.py
├── templates/
│   └── index.html
├── static/
│   └── music/
└── README.md
```

## How It Works

1. The user selects a genre in the browser.
2. Flask sends the selected genre to the backend.
3. The app generates synthetic waveform-based music using NumPy.
4. Each track is saved as a `.wav` file in `static/music/`.
5. The generated tracks are displayed with audio players and download links.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Music-Generator.git
cd AI-Music-Generator
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask numpy scipy
```

## Run the App

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Notes

- Generated files are stored in `static/music/`.
- Old generated songs are deleted each time a new set is created.
- The app currently runs with Flask debug mode enabled.

## Future Improvements

- Add MP3 export support
- Add volume and duration controls
- Improve melody generation logic
- Save generation history
- Add a `requirements.txt` file

## License

This project is open source and available under the MIT License.
