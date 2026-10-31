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