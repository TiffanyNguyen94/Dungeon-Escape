"""
Program: Dungeon Escape
Author: Tiffany Nguyen
Purpose: Defines Character, Player, and Enemy classes
Date: 10/30/2026
"""

class Character:
    """Represent a character with health and attack power."""

    def __init__(self, name, health, attack_power):
        """Initialize a character's name, health, and attack power."""
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        """Reduce health by taking damage, without going below zero."""
        self.health = max(0, self.health - damage)

    def is_alive(self):
        """Return True if character still has health."""
        return self.health > 0

    def attack(self, target):
        """Attack another character and return damage delt."""
        target.take_damage(self.attack_power)
        return self.attack_power

class Player(Character):
    """Represent a player who can use healing potions."""

    def __init__(self, name):
        """Initialize the player with default stats and potions."""
        super().__init__(name, 100, 15)
        self.potions = 2

    def heal(self):
        """Use a potion to restore health."""
        if self.potions <= 0:
            return 0

        if self.health >= self.max_health:
            return 0

        old_health = self.health

        self.health = min(self.max_health, self.health + 30)
        self.potions -= 1

        return self.health - old_health

class Enemy(Character):
    """Represent an enemy"""

    def __init__(self, name, health, attack_power, enemy_type):
        """Initialize an enemy with its stats and type."""
        super().__init__(name, health, attack_power)
        self.enemy_type = enemy_type

    def get_description(self):
        """Return a short discription of the enemy."""
        return f"A {self.enemy_type} named {self.name} appears!"