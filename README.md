# Project 2 - Text-based Dungeon RPG

This repository contains my Project 2 idea for the Python programming course. I chose Option B (Brand New Project)

## Project idea

A command-line RPG where the player explores a small dungeon, fights monsters, collects healing potions, and attempts to defeat a final boss before running out of health.


The core gameplay concept begins with a player entering 5 rooms. Each room comes with a challenge, that being an enemy encouter or discovering healing potions. The player must survive all rooms and defeat the final boss to win.


## Link to video presentation 
https://www.youtube.com/watch?v=KAX1y0tINPA


## Features
- Turn-based combat
- Player and enemy classes
- Five dungeon rooms
- Healing potions
- Save and load game progress using JSON
- Automated testing with pytest

## Installation

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Install the required dependencies:

   python -m pip install -r requirements.txt

## Running the Game
Run the following command:

   python main.py

Follow the on-screen instructions to create or load
a character and begin playing.

## Running Tests

Run the automated tests with:

   python -m pytest -v

The tests cover character attributes, combat mechanics,
healing, dungeon progression, and game persistence.