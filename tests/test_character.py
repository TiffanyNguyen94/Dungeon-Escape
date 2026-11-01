"""
Program: Dungeon Escape
Author: Tiffany Nguyen
Purpose: Tests the base Character class.
Pytest documentation
"""

from character import Character

from character import Character, Player, Enemy

def test_take_damage():
    """Verify that taking damage reduces health."""
    hero = Character("Hero", 100, 15)

    hero.take_damage(25)

    assert hero.health == 75

def test_health_not_negative():
    """Verify that health cannot drop below zero."""
    hero = Character("Hero", 100, 15)

    hero.take_damage(150)

    assert hero.health == 0

def test_is_alive():
    """Verify that character's alive status is correct."""
    hero = Character("Hero", 100, 15)

    assert hero.is_alive() is True

    hero.take_damage(100)

    assert hero.is_alive() is False

def test_attack():
    """Verify that attacks reduce target's health."""
    hero = Character("Hero", 100, 15)
    goblin = Character("Goblin", 30, 6)

    damage = hero.attack(goblin)

    assert damage == 15
    assert goblin.health == 15

def test_player_default_stats():
    """Verify that a new player has the correct starting stats."""
    player = Player("Hero")

    assert player.health == 100
    assert player.max_health == 100
    assert player.attack_power == 15
    assert player.potions == 2

def test_player_healing():
    """Verify that using potions restores health"""
    player = Player("Hero")
    player.take_damage(50)

    recovered = player.heal()

    assert recovered == 30
    assert player.health == 80
    assert player.potions == 1

def test_healing_max_health():
    """Verify that healing can't exceed max HP"""
    player = Player("Hero")
    player.take_damage(10)

    recovered = player.heal()

    assert recovered == 10
    assert player.health == 100
    assert player.potions == 1

def test_healing_at_full_health():
    """Verify that a potion is not used at full HP"""
    player = Player("Hero")

    recovered = player.heal()

    assert recovered == 0
    assert player.health == 100
    assert player.potions == 2

def test_healing_without_potions():
    """Verify that a player cannot heal without potions."""
    player = Player("Hero")
    player.take_damage(50)
    player.potions = 0

    recovered = player.heal()

    assert recovered == 0
    assert player.health == 50


def test_enemy_creation():
    """Verify that enemy attributes are initialized correctly."""
    goblin = Enemy("Bob", 30, 6, "Goblin")

    assert goblin.name == "Bob"
    assert goblin.health == 30
    assert goblin.attack_power == 6
    assert goblin.enemy_type == "Goblin"


def test_enemy_description():
    """Verify that enemies return the correct description."""
    goblin = Enemy("Bob", 30, 6, "Goblin")

    assert goblin.get_description() == "A Goblin named Bob appears!"


def test_inheritance():
    """Verify that Player and Enemy inherit from Character."""
    player = Player("Hero")
    goblin = Enemy("Bob", 30, 6, "Goblin")

def test_defeated_player_cannot_heal():
    """Verify that defeated players cannot use healing potions."""
    player = Player("Hero")
    player.take_damage(100)

    recovered = player.heal()

    assert recovered == 0
    assert player.health == 0
    assert player.potions == 2