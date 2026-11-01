"""
Program: Dungeon Escape
Author: Tiffany Nguyen
Purpose: Test combat, dungeon progression, game outcomes.
Resources: pytest documentation
Date: 10/31/2026
"""

from game import Game

def test_game_initialization():
    """Verify that a new game starts in the first room."""
    game = Game("Hero")

    assert game.player.name == "Hero"
    assert game.current_room == 1
    assert game.enemy.enemy_type == "Goblin"
    assert game.status == "playing"

def test_player_attack():
    """Verify that attcking damges the enemy and triggers retaliation."""
    game = Game("Hero")

    game.player_attack()

    assert game.enemy.health == 15
    assert game.player.health == 94

def test_room_progression():
    """Verify that defeating an enemy advances the room."""
    game = Game("Hero")

    game.player_attack()
    game.player_attack()

    assert game.current_room == 2
    assert game.enemy.name == "Gobta"
    assert game.enemy.health == 30

def test_use_potion():
    """Verify that a potion heals the player and uses a turn"""
    game = Game("Hero")
    game.player.take_damage(50)

    game.use_potion()

    assert game.player.health == 74
    assert game.player.potions == 1

def test_no_potion_at_full_health():
    """Verify that an unused potion does not trigger an enemy attck."""
    game = Game("Hero")

    game.use_potion()

    assert game.player.health == 100
    assert game.player.potions == 2

def test_final_boss_victory():
    """Verify that defeating the final boss wins the game."""
    game = Game("Hero")

    game.current_room = 5
    game.enemy = game.create_enemy()
    game.enemy.health = 15

    game.player_attack()

    assert game.status == "won"
    assert game.enemy is None
    assert game.is_over() is True

def test_player_defeat():
    """Verify that the games ends when the player loses all HP."""
    game = Game("Hero")

    game.player.health = 5
    game.player_attack()

    assert game.player.health == 0
    assert game.status == "lost"
    assert game.is_over() is True

def test_no_attacks_after_game_over():
    """Verify that defeated players cannot continue playing."""
    game = Game("Hero")
    game.status = "lost"
    original_health = game.enemy.health

    result = game.player_attack()

    assert result == "The game is already over."
    assert game.enemy.health == original_health