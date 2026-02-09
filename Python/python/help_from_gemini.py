import random as r
import time as t

class Game:
    position = 25
    quantity_positions = 4

    def __init__(self, name: str, health: int = 100,
                 skill_1_name: str = "Basic Attack", attack_min_1: int = 20, attack_max_1: int = 35,
                 skill_2_name: str = "Strong Attack", attack_min_2: int = 30, attack_max_2: int = 50,
                 is_player_char: bool = True,
                 dodge_chance: int = 0,
                 skill_1_uses: int = 10, skill_2_uses: int = 7
                 ) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.skill_1_name = skill_1_name
        self.attack_min_1 = attack_min_1
        self.attack_max_1 = attack_max_1
        self.skill_2_name = skill_2_name
        self.attack_min_2 = attack_min_2
        self.attack_max_2 = attack_max_2
        self.is_player_char = is_player_char
        self.is_defeated = False
        self.potions = {"healing_potion": 2}
        self.dodge_chance = dodge_chance
        self.skill_1_uses = skill_1_uses
        self.skill_2_uses = skill_2_uses
        self.can_revive = False
        self.revive_used = False


    def show_status(self) -> None:
        if not self.is_defeated:
            print(f"{self.name:<15}{self.health}/{self.max_health:<20} ")
        else:
            print(f"Name: {self.name} (DEFEATED)")

    def take_damage(self, damage: float, attacker_skill_name: str = "an attack") -> None:
        if self.dodge_chance > 0 and r.randint(1, 100) <= self.dodge_chance:
            print(f"{self.name} skillfully dodged the {attacker_skill_name}!")
            return

        if damage > 0:
            self.health -= damage
            if self.health < 0:
                self.health = 0
            print(f"{self.name} took {damage:.0f} damage from {attacker_skill_name}. {self.name}'s current health: {self.health}")
            if self.health == 0:
                print(f"{self.name} has been defeated!")
                self.is_defeated = True

    def give_attack(self, target, skill_choice: int) -> None:
        attack_min = 0
        attack_max = 0
        skill_name = ""
        skill_uses_remaining = 0

        if skill_choice == 1:
            skill_uses_remaining = self.skill_1_uses
            if skill_uses_remaining <= 0:
                print(f"{self.name} has no uses left for {self.skill_1_name}!")
                return
            attack_min = self.attack_min_1
            attack_max = self.attack_max_1
            skill_name = self.skill_1_name
            self.skill_1_uses -= 1
        elif skill_choice == 2:
            skill_uses_remaining = self.skill_2_uses
            if skill_uses_remaining <= 0:
                print(f"{self.name} has no uses left for {self.skill_2_name}!")
                return
            attack_min = self.attack_min_2
            attack_max = self.attack_max_2
            skill_name = self.skill_2_name
            self.skill_2_uses -= 1
        else:
            print("Invalid skill choice.")
            return

        actual_damage = r.randint(attack_min, attack_max)

        if self.name == "Mage" and skill_choice == 2 and target.name == "Dragon":
            bonus_damage = actual_damage * 0.15
            actual_damage += bonus_damage
            print(f"--> Mage's {skill_name} is 15% stronger against Dragon! (+{bonus_damage:.0f} damage)")

        if self.name == "Dragon" and target.name == "Heroe":
            bonus_damage = actual_damage * 0.25
            actual_damage += bonus_damage
            print(f"--> Dragon deals 25% extra damage to Heroe! (+{bonus_damage:.0f} damage)")

        print(f"{self.name} uses {skill_name} on {target.name} for {actual_damage:.0f} damage!")
        target.take_damage(actual_damage, skill_name)


    def heal(self, amount: int, target_char=None) -> None:
        if target_char is None:
            target_char = self

        if target_char.is_defeated:
            print(f"{target_char.name} is defeated and cannot be healed normally.")
            return

        old_health = target_char.health
        target_char.health += amount
        if target_char.health > target_char.max_health:
            target_char.health = target_char.max_health

        healed_amount = target_char.health - old_health
        if healed_amount > 0:
            print(f"{self.name} healed {target_char.name} by {healed_amount}. {target_char.name}'s current health: {target_char.health}")
        else:
            print(f"{target_char.name} is already at full health.")

    def use_potion(self, potion_type: str = "healing_potion") -> None:
        if self.is_defeated:
            print(f"{self.name} is defeated and cannot use potions.")
            return

        if self.potions.get(potion_type, 0) > 0:
            if potion_type == "healing_potion":
                healing_amount = 50
                self.heal(healing_amount, self)
                self.potions[potion_type] -= 1
                print(f"{self.name} used a {potion_type}. Remaining: {self.potions[potion_type]}")
            else:
                print(f"Unknown potion type: {potion_type}")
        else:
            print(f"{self.name} has no {potion_type}s left!")

    def revive_ally(self, target_char):
        if not self.can_revive:
            print(f"{self.name} cannot revive allies.")
            return
        if self.revive_used:
            print(f"{self.name} has already used their one-time revive ability.")
            return
        if not target_char.is_defeated:
            print(f"{target_char.name} is not defeated and does not need reviving.")
            return
        if target_char.health > 0:
            print(f"{target_char.name} is not defeated.")
            return

        revive_health = 0.3 * target_char.max_health
        target_char.health = int(revive_health)
        target_char.is_defeated = False
        self.revive_used = True
        print(f"{self.name} successfully revived {target_char.name} with {target_char.health} health!")


# --- Character Definitions ---
c1 = Game(name="Heroe", health=100, skill_1_name="Rapier Slash", attack_min_1=30, attack_max_1=41,
          skill_2_name="Blade Storm", attack_min_2=50, attack_max_2=61, dodge_chance=20,
          skill_1_uses=20, skill_2_uses=7)

c2 = Game(name="Mage", health=100, skill_1_name="Fireball", attack_min_1=34, attack_max_1=43,
          skill_2_name="Gremory Blast", attack_min_2=40, attack_max_2=70, dodge_chance=20,
          skill_1_uses=20, skill_2_uses=3)

c3 = Game(name="Axeman", health=100, skill_1_name="Axe Chop", attack_min_1=40, attack_max_1=55,
          skill_2_name="Berserk Strike", attack_min_2=60, attack_max_2=80, dodge_chance=15,
          skill_1_uses=20, skill_2_uses=7)

# New Healer character with lower health and high dodge
healer = Game(name="Cleric", health=90, # Even lower health than before
              skill_1_name="Weak Strike", attack_min_1=10, attack_max_1=20,
              skill_2_name="Holy Beam", attack_min_2=15, attack_max_2=25,
              dodge_chance=75, # Significantly increased dodge chance
              skill_1_uses=20, skill_2_uses=7)
healer.can_revive = True

dragon = Game(name="Dragon", health=300, is_player_char=False,
              skill_1_name="Fire Breath", attack_min_1=40, attack_max_1=70,
              skill_2_name="Tail Whip", attack_min_2=25, attack_max_2=80, dodge_chance=15,
              skill_1_uses=30, skill_2_uses=15)

player_characters = [c1,c2,c3, healer]

print("----Start the game------")

while True:
    print("\n--- Turn Start ---")
    print("Your Characters Status:")
    print(f"{"Name":<15}{"Health":<20} ")
    print()
    for char in player_characters:
        char.show_status()
    dragon.show_status()
    print("-" * 25)

    active_player_chars = [char for char in player_characters if not char.is_defeated]

    if not active_player_chars:
        print("All your characters have been defeated! You lost!")
        break

    print("Choose a character to act:")
    for i, char in enumerate(active_player_chars):
        print(f"{i + 1}. {char.name}")

    chosen_char = None
    while chosen_char is None:
        try:
            choice_index = int(input("Enter number: ")) - 1
            if 0 <= choice_index < len(active_player_chars):
                chosen_char = active_player_chars[choice_index]
            else:
                print("Invalid number. Please choose a valid character.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\n{chosen_char.name}'s turn. Choose an action:")
    print(f"1. {chosen_char.skill_1_name} (Damage: {chosen_char.attack_min_1}-{chosen_char.attack_max_1}, Uses: {chosen_char.skill_1_uses})")
    print(f"2. {chosen_char.skill_2_name} (Damage: {chosen_char.attack_min_2}-{chosen_char.attack_max_2}, Uses: {chosen_char.skill_2_uses})")
    print(f"3. Use Healing Potion ({chosen_char.potions.get('healing_potion', 0)} available)")
    print("\r")

    if chosen_char.name == "Cleric":
        print(f"4. Heal an Ally (Restores Health to a chosen ally)")
        if not chosen_char.revive_used:
            print(f"5. Revive an Ally (One-time use to restore a defeated ally)")

    action_choice = None
    valid_actions = ['1', '2', '3']
    if chosen_char.name == "Cleric":
        valid_actions.append('4')
        if not chosen_char.revive_used:
            valid_actions.append('5')
    print("\r")


    while action_choice not in valid_actions:
        action_choice = input("Enter action number: ").strip()
        if action_choice not in valid_actions:
            print("Invalid action choice. Please enter a valid number.")
    print("\r")

    if action_choice == '1':
        chosen_char.give_attack(dragon, 1)
    elif action_choice == '2':
        chosen_char.give_attack(dragon, 2)
    elif action_choice == '3':
        chosen_char.use_potion("healing_potion")
    elif action_choice == '4' and chosen_char.name == "Cleric":
        target_ally = None
        heal_targets = [char for char in player_characters if char != chosen_char and not char.is_defeated]
        if not heal_targets:
            print("No allies to heal that are not defeated and not yourself.")
        else:
            print("Choose an ally to heal:")
            for i, char in enumerate(heal_targets):
                print(f"{i + 1}. {char.name}")
            while target_ally is None:
                try:
                    ally_choice_index = int(input("Enter number: ")) - 1
                    if 0 <= ally_choice_index < len(heal_targets):
                        target_ally = heal_targets[ally_choice_index]
                    else:
                        print("Invalid number. Please choose a valid ally.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            if target_ally:
                chosen_char.heal(r.randint(40, 70), target_ally)
    elif action_choice == '5' and chosen_char.name == "Cleric" and not chosen_char.revive_used:
        revive_targets = [char for char in player_characters if char != chosen_char and char.is_defeated]
        if not revive_targets:
            print("No defeated allies to revive.")
        else:
            print("Choose an ally to revive:")
            for i, char in enumerate(revive_targets):
                print(f"{i + 1}. {char.name}")
            target_revive = None
            while target_revive is None:
                try:
                    revive_choice_index = int(input("Enter number: ")) - 1
                    if 0 <= revive_choice_index < len(revive_targets):
                        target_revive = revive_targets[revive_choice_index]
                    else:
                        print("Invalid number. Please choose a valid ally.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            if target_revive:
                chosen_char.revive_ally(target_revive)


    if dragon.is_defeated:
        print("\nDragon has been defeated! You win!!")
        break

    t.sleep(3)
    print("\r")

    print("\n--- Dragon's Turn ---")
    dragon_target = None
    while dragon_target is None:
        active_player_chars_for_dragon = [char for char in player_characters if not char.is_defeated]
        if not active_player_chars_for_dragon:
            break

        dragon_target = r.choice(active_player_chars_for_dragon)

    if dragon_target:
        dragon_skill_choice = r.choice([1, 2])
        dragon.give_attack(dragon_target, dragon_skill_choice)
    else:
        print("No active targets for Dragon. Game Over.")
        break
    t.sleep(2)

    if all(char.is_defeated for char in player_characters):
        print("All your characters have been defeated! You lost!")
        break

print("\n---- Game Over ----")
for char in player_characters:
    char.show_status()
dragon.show_status()