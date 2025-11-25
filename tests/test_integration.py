"""
Integration tests for the RPG game.

Integration tests focus on testing how components work together:
- fight() function with Character objects
- Complete battle scenarios
"""

from rpg.main import Character, fight


class TestFight:
    """Integration tests for the fight() function."""

    def test_fight_stronger_unit_wins(self):
        """Test that a much stronger unit wins the fight."""
        strong = Character("Strong", 100, 20, 20, 10)
        weak = Character("Weak", 1, 1, 1, 1)
        result = fight(strong, weak)
        assert "Strong wins!" in result

    def test_fight_with_equal_units(self):
        """Test fight between equal units (one should win eventually)."""
        unit1 = Character("Fighter1", 10, 15, 10, 2)
        unit2 = Character("Fighter2", 10, 15, 10, 2)
        result = fight(unit1, unit2)
        # One of them should win
        assert "Fighter1 wins!" in result or "Fighter2 wins!" in result

    def test_fight_modifies_hit_points(self):
        """Test that the fight function modifies character hit points."""
        hero = Character("Hero", 20, 15, 10, 3)
        enemy = Character("Enemy", 20, 15, 10, 3)
        
        original_hero_hp = hero.hit_points
        original_enemy_hp = enemy.hit_points
        
        fight(hero, enemy)
        
        # At least one should have lost hit points
        assert hero.hit_points < original_hero_hp or enemy.hit_points < original_enemy_hp

    def test_fight_ends_when_unit_defeated(self):
        """Test that fight ends when one unit reaches 0 or below hit points."""
        hero = Character("Hero", 5, 20, 5, 3)
        enemy = Character("Enemy", 5, 20, 5, 3)
        
        result = fight(hero, enemy)
        
        # Fight should end with one unit at 0 or below HP
        assert hero.hit_points <= 0 or enemy.hit_points <= 0
        assert isinstance(result, str)
        assert "wins!" in result

    def test_fight_with_high_defense_units(self):
        """Test fight where units have very high defense (harder to hit)."""
        tank1 = Character("Tank1", 15, 10, 25, 2)
        tank2 = Character("Tank2", 15, 10, 25, 2)
        
        result = fight(tank1, tank2)
        
        # Should still produce a winner
        assert "Tank1 wins!" in result or "Tank2 wins!" in result

    def test_fight_returns_string(self):
        """Test that fight() returns a string result."""
        unit1 = Character("A", 10, 15, 10, 2)
        unit2 = Character("B", 10, 15, 10, 2)
        
        result = fight(unit1, unit2)
        
        assert isinstance(result, str)
        assert "wins!" in result
