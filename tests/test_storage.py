"""
Program: Dungeon Escape
Author: Tiffany Nguyen
Purpose: Test saving, loading, and handling invalid game data.
Pytest documantation
Date: 11/01/2026
"""

import json

import pytest

from game import Game
from storage import save_game, load_game


def test_save_game(tmp_path):
    """Verify that saving creates a JSON file with game data."""
    game = Game("Hero")
    save_file = tmp_path / "savegame.json"

    save_game(game, save_file)

    assert save_file.exists()

    with save_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    assert data["player"]["name"] == "Hero"
    assert data["player"]["health"] == 100
    assert data["current_room"] == 1
    assert data["enemy_health"] == 30


def test_load_game(tmp_path):
    """Verify that a saved game can be loaded correctly."""
    game = Game("Hero")
    game.player.take_damage(25)
    game.player.potions = 1
    game.current_room = 3
    game.enemy = game.create_enemy()
    game.enemy.health = 20

    save_file = tmp_path / "savegame.json"

    save_game(game, save_file)
    loaded_game = load_game(save_file)

    assert isinstance(loaded_game, Game)
    assert loaded_game.player.name == "Hero"
    assert loaded_game.player.health == 75
    assert loaded_game.player.potions == 1
    assert loaded_game.current_room == 3
    assert loaded_game.enemy.health == 20


def test_missing_save_file(tmp_path):
    """Verify that loading a missing file raises a useful error."""
    save_file = tmp_path / "missing.json"

    with pytest.raises(ValueError, match="No saved game"):
        load_game(save_file)


def test_corrupted_json(tmp_path):
    """Verify that malformed JSON is handled gracefully."""
    save_file = tmp_path / "savegame.json"
    save_file.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(ValueError, match="Could not read"):
        load_game(save_file)


def test_missing_save_data(tmp_path):
    """Verify that required fields must be present."""
    save_file = tmp_path / "savegame.json"

    save_file.write_text(
        json.dumps({"player": {"name": "Hero"}}),
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="missing or invalid"):
        load_game(save_file)


def test_invalid_health(tmp_path):
    """Verify that saved health cannot exceed the maximum."""
    game = Game("Hero")
    save_file = tmp_path / "savegame.json"

    save_game(game, save_file)

    with save_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    data["player"]["health"] = 500

    with save_file.open("w", encoding="utf-8") as file:
        json.dump(data, file)

    with pytest.raises(ValueError, match="Invalid player health"):
        load_game(save_file)
