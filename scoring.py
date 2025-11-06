"""
Scoring System for The Application Game
Tracks score, combos, and bonuses
"""

import time
from colorama import Fore, Style

class ScoringSystem:
    def __init__(self):
        self.score = 0
        self.combo = 0
        self.max_combo = 0
        self.perfect_answers = 0
        self.total_answers = 0
        self.start_time = time.time()
        self.question_times = []

    def calculate_question_score(self, time_remaining, time_limit, is_correct):
        """Calculate score for a single question"""
        base_score = 100

        if not is_correct:
            self.combo = 0
            return 0

        # Correct answer bonuses
        self.combo += 1
        if self.combo > self.max_combo:
            self.max_combo = self.combo

        # Time bonus - faster answers get more points
        time_bonus = int((time_remaining / time_limit) * 50)

        # Combo multiplier
        combo_multiplier = min(self.combo, 10)  # Cap at 10x

        total_score = (base_score + time_bonus) * combo_multiplier

        self.perfect_answers += 1
        self.total_answers += 1

        return total_score

    def add_captcha_bonus(self, success):
        """Add bonus for completing CAPTCHA"""
        if success:
            bonus = 500
            self.score += bonus
            return bonus
        else:
            # Small penalty but not combo breaking
            self.score = max(0, self.score - 100)
            return -100

    def add_level_completion_bonus(self, level_number, time_taken):
        """Add bonus for completing a level"""
        base_bonus = 1000 * level_number

        # Speed bonus - complete under time pressure
        if time_taken < 60:
            speed_bonus = 2000
        elif time_taken < 120:
            speed_bonus = 1000
        else:
            speed_bonus = 500

        # Accuracy bonus
        if self.total_answers > 0:
            accuracy = self.perfect_answers / self.total_answers
            accuracy_bonus = int(1000 * accuracy)
        else:
            accuracy_bonus = 0

        # Combo bonus
        combo_bonus = self.max_combo * 100

        total_bonus = base_bonus + speed_bonus + accuracy_bonus + combo_bonus
        self.score += total_bonus

        return {
            "total": total_bonus,
            "base": base_bonus,
            "speed": speed_bonus,
            "accuracy": accuracy_bonus,
            "combo": combo_bonus
        }

    def get_score(self):
        """Get current score"""
        return self.score

    def get_combo(self):
        """Get current combo"""
        return self.combo

    def add_score(self, points):
        """Add points to score"""
        self.score += points

    def get_statistics(self):
        """Get game statistics"""
        return {
            "score": self.score,
            "combo": self.combo,
            "max_combo": self.max_combo,
            "perfect_answers": self.perfect_answers,
            "total_answers": self.total_answers,
            "accuracy": (self.perfect_answers / self.total_answers * 100) if self.total_answers > 0 else 0
        }

    def show_bonus_breakdown(self, bonuses):
        """Display bonus breakdown"""
        print(f"\n{Fore.YELLOW}╔═══════════════════════════════════════╗")
        print(f"║        💰 BONUS BREAKDOWN 💰          ║")
        print(f"╠═══════════════════════════════════════╣")
        print(f"║  Base Completion:   +{bonuses['base']:,}".ljust(41) + "║")
        print(f"║  Speed Bonus:       +{bonuses['speed']:,}".ljust(41) + "║")
        print(f"║  Accuracy Bonus:    +{bonuses['accuracy']:,}".ljust(41) + "║")
        print(f"║  Max Combo Bonus:   +{bonuses['combo']:,}".ljust(41) + "║")
        print(f"╠═══════════════════════════════════════╣")
        print(f"║  TOTAL BONUS:       +{bonuses['total']:,}".ljust(41) + "║")
        print(f"╚═══════════════════════════════════════╝{Style.RESET_ALL}\n")

    def show_final_statistics(self):
        """Show final game statistics"""
        stats = self.get_statistics()
        total_time = int(time.time() - self.start_time)

        print(f"\n{Fore.CYAN}╔═══════════════════════════════════════════════╗")
        print(f"║          📊 FINAL STATISTICS 📊               ║")
        print(f"╠═══════════════════════════════════════════════╣")
        print(f"║  Final Score:        {stats['score']:,}".ljust(48) + "║")
        print(f"║  Max Combo:          x{stats['max_combo']}".ljust(48) + "║")
        print(f"║  Accuracy:           {stats['accuracy']:.1f}%".ljust(48) + "║")
        print(f"║  Perfect Answers:    {stats['perfect_answers']}/{stats['total_answers']}".ljust(48) + "║")
        print(f"║  Total Time:         {total_time}s".ljust(48) + "║")
        print(f"╚═══════════════════════════════════════════════╝{Style.RESET_ALL}\n")
