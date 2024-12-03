# Shaik Fahad
# Nov 19, 2024

# Milestone 3, creating a game

import random

def chapter_intro(chapter_num, intro_text):
    print(f" Chapter {chapter_num} ")
    print(intro_text)
    input("Press Enter to continue...")

# crafting
def craft_item():
    items = ["Trap", "Sword", "Shield"]
    crafted = random.choice(items)
    print(f"You crafted a {crafted}!")
    return crafted

# Function to simulate a fight
def fight(enemy_name, player_health, enemy_health):
    print(f"A wild {enemy_name} appears! Prepare for battle.")
    while player_health > 0 and enemy_health > 0:
        action = input("Choose action (attack/dodge/run): ").lower()
        if action == "attack":
            damage = random.randint(5, 15)
            enemy_health -= damage
            print(f"You hit the {enemy_name} for {damage} damage. Enemy health: {enemy_health}")
        elif action == "dodge":
            print(f"You dodged the {enemy_name}'s attack!")
        elif action == "run":
            print(f"You tried to run, but the {enemy_name} blocks your path!")
            continue
        else:
            print("Invalid action. The enemy attacks!")
        
        
        enemy_damage = random.randint(5, 10)
        player_health -= enemy_damage
        print(f"The {enemy_name} hits you for {enemy_damage} damage. Your health: {player_health}")
    
    if player_health > 0:
        print(f"You defeated the {enemy_name}!")
        return True
    else:
        print("You have been defeated. Game Over.")
        return False


def start_game():
    
    player_name = input("Enter your name, adventurer: ").strip()
    print(f"Welcome, {player_name}! Let the adventure begin...")

    
    player_health = 100
    backpack = []
    
    # Chapter 1
    chapter_intro(1, "Unease in the village, villagers talk of monsters.")
    print(f"{player_name}, you decide to track a dangerous wolf through footprints and scent.")
    backpack.extend(["Rope", "Knife", "Torch"])
    print(f"Tools added to your backpack: {', '.join(backpack)}")

    # fight with wolf in Chapter 1
    if not fight("Wolf", player_health, 50):
        return  # Game over if lost the fight

    print(f"Move to the 2nd chapter...")

    # Chapter 2
    chapter_intro(2, "You enter the forest, noticing an unsettling atmosphere.")
    print(f"While exploring the forest, you discover a hidden secret cave.")
    
    
    print("Inside the cave, you find a valuable item: a Healing Potion!")
    backpack.append("Healing Potion")
    print(f"Valuable item added to your backpack: Healing Potion")
    
    if input("Do you want to set traps for monsters? (yes/no): ").lower() == "yes":
        backpack.append(craft_item())
    else:
        print("You decide not to craft traps.")
    
    print(f"Nest Chapter ahead...")

    # Fight with a monster
    if input("You hear growling nearby. Do you investigate? (yes/no): ").lower() == "yes":
        if not fight("Wolf", player_health, 50):
            return  # Game over if lost the fight

    # Chapter 3
    chapter_intro(3, "You meet an unexpected hunter ally.")
    if input("Do you want to join the hunt with the ally? (yes/no): ").lower() == "yes":
        print("You team up and defeat smaller creatures, gathering materials.")
        backpack.append(craft_item())
    else:
        print("You continue solo, crafting new weapons from gathered materials.")
        backpack.append(craft_item())
    
    print(f"Moving to the next chapter...")

    # Chapter 4
    chapter_intro(4, "The earth trembles as you prepare for a final battle.")
    guardian_health = 80
    print("You use your crafted gear and allies to weaken the Forest Guardian.")
    if fight("Forest Guardian", player_health, guardian_health):
        print("Victory! You defeated the Forest Guardian!")
    else:
        return  # Game over if lost the fight

    print(f"You choose to move further to the next chapter...")

    # Chapter 5 - The Final Choice
    chapter_intro(5, "You uncover the truth behind the forest's curse.")
    print("Do you want to save the forest or control its forces?")
    final_choice = input("Choose your path (save/control): ").lower()
    if final_choice == "save":
        print("You restore balance to the land. The villagers are safe once more.")
    else:
        print("You control the forest's forces for good, becoming its new protector.")
    
    print("\n== The End ==")
    print("Thank you for playing!")

# Start the game
start_game()
