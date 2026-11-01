"""
Program: Dungeon Escape
Author: Tiffany Nguyen
Purpose: Manage dungeon progression, combat, and game outcomes
Date:10/30/2026
"""

from character import Player, Enemy

class Game:
    """Manage the player's progress through the dungeon."""

    ROOMS = [
        ("Bob", 30, 6, "Goblin"),
        ("Gobta", 30, 6, "Goblin"),
        ("Ghost Rider", 45, 8, "Skeleton"),
        ("Jack Skellington", 45, 8, "Skeleton"),
        ("Ainz Ooal Gown", 80, 12, "Dungeon Boss"),
    ]

    def __init__(self, player_name):
        """Create a new game with a player and the first enemy."""
        self.player = Player(player_name)
        self.current_room = 1
        self.status = "playing"
        self.enemy = self.create_enemy()

    def create_enemy(self):
        """Create the enemy assigned to current rooms."""
        enemy_data = self.ROOMS[self.current_room - 1]
        return Enemy(*enemy_data)

    def complete_room(self):
        """Advance to the next room or finish the game."""
        if self.current_room == len(self.ROOMS):
            self.status = "won"
            self.enemy = None
            return "You defeated the Dungeon Boss! Congrats! You win!"

        self.current_room += 1
        self.enemy = self.create_enemy()

        return f"You advance to Room {self.current_room}!"

    def enemy_turn(self):
        """Habe the current enemy attack player."""
        damage = self.enemy.attack(self.player)

        message = f"{self.enemy.name} attacks for {damage} damage!"

        if not self.player.is_alive():
            self.status = "lost"
            message += "\nYou have been defeated! Game over."\

        return message

    def player_attack(self):
        """Attack the enemy and process the results of the turn."""
        if self.status != "playing":
            return "The game is already over."

        damage = self.player.attack(self.enemy)
        message = f"You attack {self.enemy.name} for {damage} damage!"

        if not self.enemy.is_alive():
            message += f"\nYou defeated {self.enemy.name}!"
            message += "\n" + self.complete_room()
        else:
            message += "\n" + self.enemy_turn()

        return message

    def use_potion(self):
        """Use a healing and process enemy's turn."""
        if self.status != "playing":
            return "The game is already over."
        
        healed = self.player.heal()

        if healed == 0:
            return "Can't use potion right now."

        message = f"You recovered {healed} HP!"
        message += "\n" + self.enemy_turn()

        return message

    def get_status(self):
        """Return the player's curretn dungeon status."""
        return(
            f"Player: {self.player.name}\n"
            f"HP: {self.player.health}/{self.player.max_health}\n"
            f"Potions: {self.player.potions}\n"
            f"Room: {self.current_room}/{len(self.ROOMS)}"
        )

    def is_over(self):
        """Return True if the game has ended."""
        return self.status != "playing"