"""
Game State Management for The Application Game
Handles saving/loading game progress, high scores, and statistics
"""

import json
import os
from datetime import datetime

class GameState:
    def __init__(self):
        self.save_file = "game_save.json"
        self.high_score = 0
        self.jobs_applied = 0
        self.unlocked_levels = 1
        self.level_high_scores = [0] * 10
        self.load_state()

    def load_state(self):
        """Load game state from save file"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as f:
                    data = json.load(f)
                    self.high_score = data.get('high_score', 0)
                    self.jobs_applied = data.get('jobs_applied', 0)
                    self.unlocked_levels = data.get('unlocked_levels', 1)
                    self.level_high_scores = data.get('level_high_scores', [0] * 10)
            except:
                pass

    def save_state(self):
        """Save game state to file"""
        data = {
            'high_score': self.high_score,
            'jobs_applied': self.jobs_applied,
            'unlocked_levels': self.unlocked_levels,
            'level_high_scores': self.level_high_scores
        }
        with open(self.save_file, 'w') as f:
            json.dump(data, f, indent=2)

    def increment_jobs_applied(self):
        """Increment the jobs applied counter"""
        self.jobs_applied += 1
        self.save_state()

    def update_high_score(self, score):
        """Update high score if new score is higher"""
        if score > self.high_score:
            self.high_score = score
            self.save_state()
            return True
        return False

    def update_level_score(self, level, score):
        """Update level high score"""
        if score > self.level_high_scores[level - 1]:
            self.level_high_scores[level - 1] = score
            self.save_state()
            return True
        return False

    def unlock_level(self, level):
        """Unlock a level"""
        if level > self.unlocked_levels:
            self.unlocked_levels = level
            self.save_state()
