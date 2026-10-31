"""Tests the base Character class."""

from character import Character

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