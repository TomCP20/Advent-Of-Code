# make sure to run from the aoc reppo!

import os
import subprocess

dirname = os.path.dirname(__file__)

year = "2024"

for i in range(4, 26):
    day_path = os.path.join(dirname, year, f"Day {i:02d}")

    #inputs
    open(os.path.join(day_path, "test.txt"), 'a').close()
    open(os.path.join(day_path, "input.txt"), 'a').close()
    #Python
    os.makedirs(os.path.join(day_path, "Python"))
    open(os.path.join(day_path, "Python", "main.py"), 'a').close()

    #C++
    os.makedirs(os.path.join(day_path, "C++"))
    open(os.path.join(day_path, "C++", "main.cpp"), 'a').close()

    #C#
    os.makedirs(os.path.join(day_path, "C#"))
    subprocess.run(["dotnet", "new", "console"], cwd=os.path.join(day_path, "C#"))

    #F#
    os.makedirs(os.path.join(day_path, "F#"))
    subprocess.run(["dotnet", "new", "console", "-lang", "F#"], cwd=os.path.join(day_path, "F#"))

    #Rust    
    os.makedirs(os.path.join(day_path, "Rust"))
    subprocess.run(["cargo", "init"], cwd=os.path.join(day_path, "Rust"))