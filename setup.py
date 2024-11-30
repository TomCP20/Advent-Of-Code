import os

year = "2024"

languages = ["Python", "C++", "F#", "Rust"]

for i in range(1, 26):
    for lang in languages:
        path = os.path.join(year, f"Day {i}", lang)
        os.mkdir(path)