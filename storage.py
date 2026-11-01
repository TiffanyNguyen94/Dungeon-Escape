"""
Program: Dungeon Escape
Author: Tiffany Nguyen
Purpose: Save and load Dungeon Escape using JSON
Date: 11/01/2026
"""

import json
from pathlib import Path

from game import Game

SAVE_FILE = Path(__file__).resolve().parent / "savegame.json"


def save_game(game, filepath=SAVE_FILE):
    """Save the current game progress to a JSON file."""
    data = {
        "player": {
            "name": game.player.name,
            "health": game.player.health,
            "potions": game.player.potions
        },
        "current_room": game.current_room,
        "enemy_health": game.enemy.health
    }

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except OSError as error:
        raise ValueError(f"Could not save the game: {error}") from error


def load_game(filepath=SAVE_FILE):
    """Load saved game progress from a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        raise ValueError("No saved game was found.")

    except (OSError, UnicodeError, json.JSONDecodeError):
        raise ValueError("Could not read the saved game.")

    try:
        player_data = data["player"]

        name = player_data["name"]
        health = player_data["health"]
        potions = player_data["potions"]
        room = data["current_room"]
        enemy_health = data["enemy_health"]

        if not name or not name.strip():
            raise ValueError("Invalid player name.")

        if health < 1 or health > 100:
            raise ValueError("Invalid player health.")

        if potions < 0:
            raise ValueError("Invalid potion count.")

        if room < 1 or room > len(Game.ROOMS):
            raise ValueError("Invalid room number.")

        game = Game(name)

        game.current_room = room
        game.enemy = game.create_enemy()

        if enemy_health < 1 or enemy_health > game.enemy.max_health:
            raise ValueError("Invalid enemy health.")

        game.player.health = health
        game.player.potions = potions
        game.enemy.health = enemy_health

        return game

    except (KeyError, TypeError, AttributeError, IndexError):
        raise ValueError("Saved game data is missing or invalid.")