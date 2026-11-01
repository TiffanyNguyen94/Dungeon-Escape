"""
Program: Dungeon Escape
Author: Tiffany Nguyen
Purpose: Provide the menus and user interface for Dungeon Escape
Date: 10/30/2026
"""

from game import Game

from storage import save_game, load_game



def show_combat_menu():
    """Display the available actions during combat."""
    print("\n1. Attack")
    print("2. Use Potion")
    print("3. View Status")
    print("4. Save Game")
    print("5. Return to Main Menu")


def play_game(game):
    """Run the interactive dungeon until the game ends or player exits"""
    print(f"\nWelcome to Dungeon Escape, {game.player.name}!")

    last_room = 0

    while not game.is_over():
        if game.current_room != last_room:
            print(f"\n=== ROOM {game.current_room}/5 ===")
            print(game.enemy.get_description())
            last_room = game.current_room

        print(f"\nYour HP: {game.player.health}/{game.player.max_health}")
        print(f"Enemy HP: {game.enemy.health}/{game.enemy.max_health}")

        show_combat_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n" + game.player_attack())

        elif choice == "2":
            print("\n" + game.use_potion())

        elif choice == "3":
            print("\n" + game.get_status())

        elif choice == "4":
            try:
                save_game(game)
                print("\nGame saved successfully!")

            except ValueError as error:
                print(f"\nSave failed: {error}")

        elif choice == "5":
            print("\nReturning to the main menu...")
            print("Unsaved progress will be lost.")
            return

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

    if game.status == "won":
        print("\nCongratulations! You escaped the dungeon! :D")
    elif game.status == "lost":
        print("\nYour adventure has ended. :(")


def start_new_game():
    """Ask for the player's name and start a new dungeon game."""
    name = input("\nEnter your character's name: ").strip()

    if not name:
        name = "Hero"

    game = Game(name)
    play_game(game)


def main():
    """Display the main menu and manage user selections."""
    while True:
        print("\n=== DUNGEON ESCAPE ===")
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            start_new_game()

        elif choice == "2":
            try:
                game = load_game()
                print("\nGame loaded successfully!")
                play_game(game)

            except ValueError as error:
                print(f"\nLoad failed: {error}")

        elif choice == "3":
            print("\nThanks for playing Dungeon Escape!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

