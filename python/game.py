import random

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.magic_points = 10
        self.max_mp = 10
        self.inventory = {"potion": 3, "mana_potion": 2}

    def attack(self, enemy):
        damage = random.randint(5, 15)
        enemy.health -= damage
        enemy.health = max(0, enemy.health)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def magic_attack(self, enemy):
        if self.magic_points > 0:
            damage = random.randint(15, 25)
            enemy.health -= damage
            self.magic_points -= 1
            enemy.health = max(0, enemy.health)
            print(f"{self.name} performs a magic attack on {enemy.name} for {damage} damage! MP left: {self.magic_points}")
        else:
            print("Not enough MP!")

    def heal(self):
        if self.inventory["potion"] > 0:
            heal_amount = random.randint(10, 20)
            self.health = min(self.max_health, self.health + heal_amount)
            self.inventory["potion"] -= 1
            print(f"{self.name} heals for {heal_amount} health! Potions left: {self.inventory['potion']}")
        else:
            print("No potions left!")

    def restore_mp(self):
        if self.inventory["mana_potion"] > 0:
            mp_restore = random.randint(3, 5)
            self.magic_points = min(self.max_mp, self.magic_points + mp_restore)
            self.inventory["mana_potion"] -= 1
            print(f"{self.name} restores {mp_restore} MP! Mana potions left: {self.inventory['mana_potion']}")
        else:
            print("No mana potions left!")

    def run_away(self):
        chance = random.randint(1, 2)
        if chance == 1:
            print(f"{self.name} successfully ran away!")
            return True
        else:
            print(f"{self.name} failed to run away!")
            return False

# Enemy class
class Enemy:
    def __init__(self, name, health, attack_power, level):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.level = level

    def melee_attack(self, player):
        damage = random.randint(5, self.attack_power)
        player.health -= damage
        player.health = max(0, player.health)
        print(f"{self.name} attacks {player.name} for {damage} damage!")

def encounter_enemy(level):
    enemies = [
        Enemy("Goblin", 30 + level * 5, 10 + level * 2, level),
        Enemy("Troll", 50 + level * 10, 15 + level * 3, level),
        Enemy("Dragon", 100 + level * 15, 20 + level * 5, level)
    ]
    return enemies[(level - 1) % 3]

def main():
    print("Welcome to the Realm of Shadows!")
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    print("Your quest begins now!")

    level = 1  # Start with level 1

    while player.health > 0:
        print(f"\nYou are exploring the realm... Level {level}")
        action = input("Press Enter to continue (or type 'q' to quit): ")
        if action.lower() == 'q':
            break

        current_enemy = encounter_enemy(level)
        print(f"A wild {current_enemy.name} (Level {current_enemy.level}) appears!")

        while player.health > 0 and current_enemy.health > 0:
            print("\nWhat do you want to do?")
            print("1. Attack")
            print("2. Magic Attack")
            print("3. Heal")
            print("4. Restore MP")
            print("5. Run Away")
            action = input("Choose an action (1/2/3/4/5): ")

            if action == "1":
                player.attack(current_enemy)
            elif action == "2":
                player.magic_attack(current_enemy)
            elif action == "3":
                player.heal()
            elif action == "4":
                player.restore_mp()
            elif action == "5":
                if player.run_away():
                    break
            else:
                print("Invalid action! Please choose 1, 2, 3, 4, or 5.")

            if current_enemy.health > 0:
                current_enemy.melee_attack(player)

            print(f"\n{player.name}'s health: {player.health}")
            print(f"{current_enemy.name} (Level {current_enemy.level})'s health: {current_enemy.health}")

        if player.health <= 0:
            print(f"\n{player.name} was defeated by the {current_enemy.name}...")
            print("The realm falls into darkness...")
            break
        elif current_enemy.health <= 0:
            print(f"\n{player.name} has defeated the {current_enemy.name} (Level {current_enemy.level})!")
            print("Victory is yours! You find a potion and a mana potion on the enemy's body.")
            player.inventory["potion"] += 1
            player.inventory["mana_potion"] += 1
            print(f"Potions in inventory: {player.inventory['potion']}")
            print(f"Mana potions in inventory: {player.inventory['mana_potion']}")
            level += 1  # Increase the level for next enemy

    if player.health > 0:
        print("Congratulations! You have survived the challenges of the realm.")
    print("Thank you for playing the Realm of Shadows! May you find peace and glory in your next adventure.")

# Run the game
if __name__ == "__main__":
    main()
