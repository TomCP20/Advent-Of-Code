"""Setup directories for advent of code, make sure to run from the aoc reppo."""

import os
import subprocess

dirname = os.path.dirname(__file__)

YEAR = 2023
DAYS = 25
INPUTS = True
PYTHON = True
CPP = False
CS = False
FS = False
RUST = False

def makefile(directory: str, name: str):
    """creates an empty file with name name in directory directory"""
    with open(os.path.join(directory, name), 'x', encoding="utf-8"):
        pass

for i in range(1, DAYS+1):
    day_path = os.path.join(dirname, str(YEAR), f"Day {i:02d}")
    os.makedirs(day_path, exist_ok=True)
    if INPUTS:
        makefile(day_path, "test.txt")
        makefile(day_path, "input.txt")
    if PYTHON:
        cwd = os.path.join(day_path, "Python")
        os.makedirs(cwd)
        with open(os.path.join(cwd, "main.py"), 'w', encoding="utf-8") as f:
            f.writelines([
                f"\"\"\"Advent of Code - {YEAR} - Day {i}\"\"\"\n\n\n",
                "def main():\n",
                f"    \"\"\"Solves Part 1 and 2 of Day {i}\"\"\"\n",
                "    with open(0, encoding=\"utf-8\") as f:\n",
                "        print(f.read().splitlines())\n\n\n"
                "main()\n"
            ])
    if CPP:
        cwd = os.path.join(day_path, "C++")
        os.makedirs(cwd)
        makefile(cwd, "main.cpp")
    if CS:
        cwd = os.path.join(day_path, "C#")
        os.makedirs(cwd)
        subprocess.run(["dotnet", "new", "console"], cwd=cwd, check=True)
    if FS:
        cwd = os.path.join(day_path, "F#")
        os.makedirs(cwd)
        subprocess.run(["dotnet", "new", "console", "-lang", "F#"], cwd=cwd, check=True)
    if RUST:
        cwd = os.path.join(day_path, "Rust")
        os.makedirs(cwd)
        subprocess.run(["cargo", "init"], cwd=cwd, check=True)
