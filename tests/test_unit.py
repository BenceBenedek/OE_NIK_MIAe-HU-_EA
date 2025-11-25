"""
Unit tests for the RPG game components.

Unit tests focus on testing individual components in isolation:
- Character class initialization
- roll() function behavior
"""

from rpg.main import Character, roll


class TestCharacter:
    """Unit tests for the Character class."""

    def test_character_creation(self):
        """Test that a Character can be created with correct attributes."""
        hero = Character("Hero", 10, 12, 12, 3)
        assert hero.name == "Hero"
        assert hero.hit_points == 10
        assert hero.attack == 12
        assert hero.defense == 12
        assert hero.damage == 3

    def test_character_with_zero_hp(self):
        """Test that a Character can be created with zero hit points."""
        dead = Character("Dead", 0, 10, 10, 1)
        assert dead.hit_points == 0

    def test_character_with_negative_values(self):
        """Test that a Character can be created with negative values."""
        weak = Character("Weak", -5, -10, -10, -1)
        assert weak.hit_points == -5
        assert weak.attack == -10


class TestRoll:
    """Unit tests for the roll() function."""

    def test_roll_returns_int(self):
        """Test that roll() returns an integer."""
        result = roll()
        assert isinstance(result, int)

    def test_roll_in_range(self):
        """Test that roll() returns a value between 1 and 20."""
        for _ in range(100):  # Test multiple times due to randomness
            result = roll()
            assert 1 <= result <= 20

    def test_roll_can_return_min_and_max(self):
        """Test that roll() can return both 1 and 20 (boundary values)."""
        results = set()
        for _ in range(1000):  # Run many times to likely hit boundaries
            results.add(roll())
        
        # After 1000 rolls, we should see both 1 and 20
        assert 1 in results
        assert 20 in results
