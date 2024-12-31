"""Setup directories for advent of code, make sure to run from the aoc reppo."""

import os
import subprocess

dirname = os.path.dirname(__file__)

YEAR = "2024"
INPUTS = True
PYTHON = True
CPP = True
CS = True
FS = True
RUST = True

def makefile(directory: str, name: str):
    """creates an empty file with name name in directory directory"""
    with open(os.path.join(directory, name), 'x', encoding="utf-8"):
        pass

for i in range(1, 26):
    day_path = os.path.join(dirname, YEAR, f"Day {i:02d}")
    if INPUTS:
        makefile(day_path, "test.txt")
        makefile(day_path, "input.txt")
    if PYTHON:
        cwd = os.path.join(day_path, "Python")
        os.makedirs(cwd)
        makefile(cwd, "main.py")
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
