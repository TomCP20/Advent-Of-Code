# make sure to run from the aoc reppo!

import os

dirname = os.path.dirname(__file__)

year = "2024"

languages = ["Python", "C++", "F#", "Rust"]

for i in range(1, 26):
    for lang in languages:
        os.makedirs(os.path.join(dirname, year, f"Day {i}", lang))