from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should never be reset.
        file_path = Path("high_score.txt")
        if file_path.is_file():
            with open('high_score.txt', 'r') as file:
                content = file.read().strip()
                self.high_score = int(content)
        else:
            self.high_score = 0


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
