"""
Simple file to implement the EA 1 assignment

Assignment Details:
Platform: Moodle
- Create your own public repository on GitHub.
- Write any single class/program and write 2 types of tests for it: ‘unit’ and ‘integration’.
- Set up GitHub Actions to run the ‘unit’ tests for pull requests.
- Set up GitHub Actions to run the ‘unit’ and ‘integration’ tests for every commit on the master branch.
- Submit your repository’s link, which should contain successful test runs on master commit, and at least one PR with passing/failing test runs.

Note: The test results are irrelevant; you just need to demonstrate that you have tests, and they run when they must.
"""

from dataclasses import dataclass
from random import randint

@dataclass
class Character:
    """A class representing a character in the RPG game.
    Attributes:
        name (str): The name of the character.
        hit_points (int): The health points of the character.
        attack (int): The attack value of the character.
        defense (int): The defense value of the character.
        damage (int): The damage the character can inflict.
    """
    name : str
    hit_points : int
    attack : int
    defense : int
    damage : int

def roll() -> int:
    """
    Simulates a roll of a 20-sided die.
    Returns a random integer between 1 and 20.
    """
    return randint(1, 20)

def fight(unit1: Character, unit2: Character) -> str:
    """
    Simulates a fight between two characters until one is defeated.
    Returns the name of the winning character.
    """
    while unit1.hit_points > 0 and unit2.hit_points > 0:

        # Unit 1 attacks Unit 2
        print(f"{unit1.name} attacks!")
        if roll() <= unit1.attack and roll() > unit2.defense:
            unit2.hit_points -= max(0, unit1.damage)
            print(f"{unit1.name} hits! Damages {unit2.name} for {unit1.damage} hit points.")
            print(f"{unit2.name} has {unit2.hit_points} hit points left.")
        else:
            print(f"{unit1.name} missed!")

        # Unit 2 attacks Unit 1
        print(f"{unit2.name} attacks!")
        if roll() <= unit2.attack and roll() > unit1.defense:
            unit1.hit_points -= max(0, unit2.damage)
            print(f"{unit2.name} hits! Damages {unit1.name} for {unit2.damage} hit points.")
            print(f"{unit1.name} has {unit1.hit_points} hit points left.")
        else:
            print(f"{unit2.name} missed!")

        if unit2.hit_points <= 0:
            return f"{unit1.name} wins!"
    return f"{unit2.name} wins!"

if __name__ == "__main__":
    player_instance = Character("Hero", 10, 12, 12, 3)
    enemy_instance = Character("Goblin", 8, 16, 16, 2)
    RESULT = fight(player_instance, enemy_instance)
    print(RESULT)
