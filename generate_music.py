import numpy as np
from scipy.io.wavfile import write
import random
import os
import uuid
import time

sample_rate = 44100


# 🎹 waveform
def sine(freq, t):
    return np.sin(2 * np.pi * freq * t)


# 🎚 envelope (smooth fade)
def envelope(signal):
    attack = int(len(signal) * 0.1)
    decay = int(len(signal) * 0.4)

    env = np.ones(len(signal))
    env[:attack] = np.linspace(0, 1, attack)
    env[-decay:] = np.linspace(1, 0, decay)

    return signal * env


# 🥁 drum
def drum(t):
    return np.exp(-10 * t) * np.random.randn(len(t)) * 0.3


def generate_music(genre):

    folder = "static/music"
    os.makedirs(folder, exist_ok=True)

    # clear old songs
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))

    songs = []
    random.seed(time.time())

    # 🎼 tempo
    genre_rules = {
        "sad":55,
        "romance":55,   # slower = emotional
        "happy":140,
        "action":160,
        "thriller":110,
        "edm":150,
        "rock":130,
        "jazz":110,
        "lofi":80,
        "ambient":50,
        "hiphop":90,
        "cinematic":70,
        "piano":75,
        "horror":60,
        "scifi":120
    }

    tempo = genre_rules.get(genre, 100)
    beat_length = 60 / tempo

    # 🎼 scales
    scales = [
        [220,247,262,294],
        [261,293,329,349],
        [392,440,494,523],
        [330,349,392,440],
        [196,220,247]
    ]

    for i in range(10):

        random.seed(time.time() + i)

        audio = np.array([])
        scale = random.choice(scales)

        steps = random.randint(20, 40)

        for step in range(steps):

            duration = beat_length * random.uniform(1, 2.5)
            t = np.linspace(0, duration, int(sample_rate * duration))

            # 💖 ROMANCE FIXED (NO SIREN SOUND)
            if genre == "romance":

                # low calm notes only
                base_notes = [196, 220, 247, 262]
                freq = random.choice(base_notes)

                # pure soft tone
                main = sine(freq, t)

                # gentle harmony
                harmony = sine(freq * 1.5, t) * 0.05

                segment = main + harmony
                segment = envelope(segment) * 0.4

            else:
                freq = random.choice(scale)

                # chord variation
                chord_type = random.choice(["major", "minor", "power"])

                if chord_type == "major":
                    main = sine(freq, t) + 0.5*sine(freq*1.25, t)

                elif chord_type == "minor":
                    main = sine(freq, t) + 0.5*sine(freq*1.2, t)

                else:
                    main = sine(freq, t) + 0.3*sine(freq*1.5, t)

                # bass
                bass = sine(freq / random.choice([2,3]), t) * random.uniform(0.3, 0.6)

                # melody
                melody = sine(freq * random.choice([1, 1.5, 2]), t) * random.uniform(0.2, 0.5)

                segment = main + bass + melody

            # 🥁 drums control
            if genre == "romance":
                pass

            elif genre in ["sad","lofi","ambient","piano"]:
                pass

            elif genre in ["action","edm","rock","hiphop"]:
                if random.random() > 0.4:
                    segment += drum(t)

            elif genre in ["thriller","scifi"]:
                if random.random() > 0.85:
                    segment += drum(t)

            # smoothing
            segment = envelope(segment)

            if genre in ["sad","romance","lofi","ambient","piano"]:
                segment = np.tanh(segment)

            audio = np.concatenate((audio, segment))

        # normalize
        audio = audio / np.max(np.abs(audio))
        audio = (audio * 32767).astype(np.int16)

        filename = f"{uuid.uuid4()}.wav"
        write(os.path.join(folder, filename), sample_rate, audio)

        songs.append(filename)

    return songs